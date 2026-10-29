"""
AI Chat API Views
"""
import json
import urllib.request
import urllib.error
from django.http import StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import os
import logging

logger = logging.getLogger(__name__)


@csrf_exempt
@require_http_methods(["POST"])
def chat_view(request):
    """
    AI Chat endpoint - handles streaming responses from SiliconFlow API
    """
    try:
        data = json.loads(request.body)
        messages = data.get('messages', [])

        api_key = os.environ.get('SILICONFLOW_API_KEY', '')
        api_base_url = os.environ.get('SILICONFLOW_API_BASE_URL', 'https://api.siliconflow.cn/v1')

        logger.info(f"AI chat request received: {len(messages)} messages")
        logger.info(f"API key configured: {bool(api_key)}")
        logger.info(f"API base URL: {api_base_url}")

        if not api_key:
            logger.error("API key not configured")
            return StreamingHttpResponse(
                iter([json.dumps({"error": "API key not configured"})]),
                content_type='application/json',
                status=500
            )

        api_url = f"{api_base_url}/chat/completions"

        request_data = json.dumps({
            "model": "deepseek-ai/DeepSeek-V4-Flash",
            "messages": messages,
            "stream": True,
            "max_tokens": 1024,
        }).encode('utf-8')

        req = urllib.request.Request(
            api_url,
            data=request_data,
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {api_key}',
            },
            method='POST'
        )

        try:
            response = urllib.request.urlopen(req, timeout=60)
        except urllib.error.HTTPError as e:
            error_body = e.read().decode('utf-8')
            return StreamingHttpResponse(
                iter([json.dumps({"error": f"API error: {error_body}"})]),
                content_type='application/json',
                status=500
            )
        except urllib.error.URLError as e:
            return StreamingHttpResponse(
                iter([json.dumps({"error": f"Connection error: {str(e)}"})]),
                content_type='application/json',
                status=500
            )

        def generate():
            try:
                for line in response:
                    line = line.decode('utf-8')
                    if line.startswith('data: '):
                        data_str = line[6:]
                        if data_str == '[DONE]':
                            continue
                        try:
                            json_data = json.loads(data_str)
                            content = json_data.get('choices', [{}])[0].get('delta', {}).get('content', '')
                            if content:
                                yield f'data: {json.dumps({"content": content})}\n\n'
                        except json.JSONDecodeError:
                            continue
            except Exception as e:
                yield f'data: {json.dumps({"error": str(e)})}\n\n'

        return StreamingHttpResponse(
            generate(),
            content_type='text/event-stream'
        )

    except json.JSONDecodeError:
        return StreamingHttpResponse(
            iter([json.dumps({"error": "Invalid JSON in request body"})]),
            content_type='application/json',
            status=400
        )
    except Exception as e:
        return StreamingHttpResponse(
            iter([json.dumps({"error": str(e)})]),
            content_type='application/json',
            status=500
        )
