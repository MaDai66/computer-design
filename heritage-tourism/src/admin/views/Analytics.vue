<template>
  <div class="analytics">
    <div class="analytics-header">
      <h2>数据分析</h2>
      <div class="date-range">
        <select v-model="dateRange">
          <option value="7">最近7天</option>
          <option value="30">最近30天</option>
          <option value="90">最近90天</option>
          <option value="365">最近一年</option>
        </select>
      </div>
    </div>

    <!-- 数据概览 -->
    <div class="stats-overview">
      <div class="stat-card">
        <div class="stat-icon revenue">💰</div>
        <div class="stat-content">
          <h3>¥{{ stats.revenue }}</h3>
          <p>总销售额</p>
          <span class="stat-change positive">+{{ stats.revenueChange }}%</span>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon orders">📦</div>
        <div class="stat-content">
          <h3>{{ stats.orders }}</h3>
          <p>订单数</p>
          <span class="stat-change positive">+{{ stats.ordersChange }}%</span>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon users">👥</div>
        <div class="stat-content">
          <h3>{{ stats.users }}</h3>
          <p>新用户</p>
          <span class="stat-change positive">+{{ stats.usersChange }}%</span>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon conversion">📈</div>
        <div class="stat-content">
          <h3>{{ stats.conversion }}%</h3>
          <p>转化率</p>
          <span class="stat-change negative">-{{ Math.abs(stats.conversionChange) }}%</span>
        </div>
      </div>
    </div>

    <!-- 销售趋势 -->
    <div class="chart-section">
      <div class="section-header">
        <h3>销售趋势</h3>
        <div class="chart-controls">
          <button 
            v-for="period in chartPeriods" 
            :key="period.value"
            :class="['period-btn', { active: activePeriod === period.value }]"
            @click="activePeriod = period.value"
          >
            {{ period.label }}
          </button>
        </div>
      </div>
      <div class="chart-container">
        <div class="sales-chart">
          <canvas ref="salesChart"></canvas>
        </div>
      </div>
    </div>

    <!-- 产品销售排行 -->
    <div class="chart-section">
      <div class="section-header">
        <h3>产品销售排行</h3>
      </div>
      <div class="products-ranking">
        <table>
          <thead>
            <tr>
              <th>排名</th>
              <th>产品</th>
              <th>销量</th>
              <th>销售额</th>
              <th>占比</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(product, index) in topProducts" :key="product.id">
              <td class="rank">{{ index + 1 }}</td>
              <td class="product-info">
                <div class="product-image">
                  <img :src="product.image" :alt="product.name" />
                </div>
                <span class="product-name">{{ product.name }}</span>
              </td>
              <td>{{ product.sales }}</td>
              <td>¥{{ product.revenue }}</td>
              <td>
                <div class="progress-bar">
                  <div 
                    class="progress-fill" 
                    :style="{ width: product.percentage + '%' }"
                  ></div>
                </div>
                <span class="percentage">{{ product.percentage }}%</span>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- 用户行为分析 -->
    <div class="chart-section">
      <div class="section-header">
        <h3>用户行为分析</h3>
      </div>
      <div class="user-behavior">
        <div class="behavior-item">
          <h4>访问来源</h4>
          <div class="pie-chart">
            <canvas ref="sourceChart"></canvas>
          </div>
        </div>
        <div class="behavior-item">
          <h4>用户设备</h4>
          <div class="pie-chart">
            <canvas ref="deviceChart"></canvas>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { adminAPI } from '../api/adminAPI'

const dateRange = ref('30')
const activePeriod = ref('day')
const salesChart = ref(null)
const sourceChart = ref(null)
const deviceChart = ref(null)
const isLoading = ref(true)

const chartPeriods = [
  { label: '按日', value: 'day' },
  { label: '按周', value: 'week' },
  { label: '按月', value: 'month' }
]

// 统计数据
const stats = ref({
  revenue: 0,
  revenueChange: 0,
  orders: 0,
  ordersChange: 0,
  users: 0,
  usersChange: 0,
  conversion: 0,
  conversionChange: 0
})

// 产品销售数据
const topProducts = ref([])

// 销售趋势数据
const salesData = ref({
  labels: [],
  datasets: [
    {
      label: '销售额',
      data: [],
      borderColor: '#3498db',
      backgroundColor: 'rgba(52, 152, 219, 0.1)',
      tension: 0.4
    }
  ]
})

// 加载概览数据
const loadOverviewData = async () => {
  isLoading.value = true
  try {
    const response = await adminAPI.analytics.getOverview({
      days: dateRange.value
    })
    stats.value = {
      revenue: response.revenue || 0,
      revenueChange: response.revenue_change || 0,
      orders: response.orders || 0,
      ordersChange: response.orders_change || 0,
      users: response.users || 0,
      usersChange: response.users_change || 0,
      conversion: response.conversion || 0,
      conversionChange: response.conversion_change || 0
    }
  } catch (error) {
    console.error('加载概览数据失败:', error)
  } finally {
    isLoading.value = false
  }
}

// 加载销售趋势数据
const loadSalesTrend = async () => {
  try {
    const response = await adminAPI.analytics.getSalesTrend({
      days: dateRange.value,
      period: activePeriod.value
    })
    salesData.value = {
      labels: response.labels || [],
      datasets: [
        {
          label: '销售额',
          data: response.data || [],
          borderColor: '#3498db',
          backgroundColor: 'rgba(52, 152, 219, 0.1)',
          tension: 0.4
        }
      ]
    }
  } catch (error) {
    console.error('加载销售趋势失败:', error)
  }
}

// 加载产品排行数据
const loadTopProducts = async () => {
  try {
    const response = await adminAPI.analytics.getTopProducts({
      days: dateRange.value,
      limit: 5
    })
    topProducts.value = response.results || []
  } catch (error) {
    console.error('加载产品排行失败:', error)
  }
}

// 加载用户行为数据
const loadUserBehavior = async () => {
  try {
    const response = await adminAPI.analytics.getUserBehavior({
      days: dateRange.value
    })
    // 这里可以处理用户行为数据
  } catch (error) {
    console.error('加载用户行为失败:', error)
  }
}

// 加载所有数据
const loadAllData = async () => {
  await Promise.all([
    loadOverviewData(),
    loadSalesTrend(),
    loadTopProducts(),
    loadUserBehavior()
  ])
}

// 日期范围变更
const handleDateRangeChange = () => {
  loadAllData()
}

// 周期变更
const handlePeriodChange = () => {
  loadSalesTrend()
}

onMounted(() => {
  // 初始加载数据
  loadAllData()
})
</script>

<style scoped>
.analytics {
  width: 100%;
}

.analytics-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
}

.analytics-header h2 {
  margin: 0;
  color: #333;
  font-size: 24px;
}

.date-range select {
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 14px;
  background: white;
}

/* 数据概览 */
.stats-overview {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin-bottom: 30px;
}

.stat-card {
  background: white;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  display: flex;
  align-items: center;
  transition: transform 0.3s, box-shadow 0.3s;
}

.stat-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.stat-icon {
  font-size: 32px;
  margin-right: 15px;
  width: 50px;
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 8px;
}

.stat-icon.revenue {
  background: #f3e5f5;
  color: #9c27b0;
}

.stat-icon.orders {
  background: #e8f5e8;
  color: #4caf50;
}

.stat-icon.users {
  background: #e3f2fd;
  color: #2196f3;
}

.stat-icon.conversion {
  background: #fff3e0;
  color: #ff9800;
}

.stat-content h3 {
  margin: 0 0 5px 0;
  font-size: 24px;
  color: #333;
}

.stat-content p {
  margin: 0 0 5px 0;
  color: #666;
  font-size: 14px;
}

.stat-change {
  font-size: 12px;
  font-weight: 500;
}

.stat-change.positive {
  color: #4caf50;
}

.stat-change.negative {
  color: #e53935;
}

/* 图表区域 */
.chart-section {
  background: white;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  margin-bottom: 30px;
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.section-header h3 {
  margin: 0;
  color: #333;
  font-size: 18px;
}

.chart-controls {
  display: flex;
  gap: 10px;
}

.period-btn {
  padding: 6px 12px;
  border: 1px solid #ddd;
  background: white;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  transition: all 0.3s;
}

.period-btn:hover {
  background: #f5f7fa;
}

.period-btn.active {
  background: #3498db;
  color: white;
  border-color: #3498db;
}

.chart-container {
  height: 300px;
  position: relative;
}

.sales-chart {
  width: 100%;
  height: 100%;
}

/* 产品销售排行 */
.products-ranking table {
  width: 100%;
  border-collapse: collapse;
}

.products-ranking th,
.products-ranking td {
  padding: 12px;
  text-align: left;
  border-bottom: 1px solid #eee;
}

.products-ranking th {
  background: #f5f7fa;
  font-weight: 600;
  color: #333;
}

.products-ranking tr:hover {
  background: #f9f9f9;
}

.rank {
  font-weight: 600;
  color: #333;
  width: 60px;
}

.product-info {
  display: flex;
  align-items: center;
  gap: 12px;
}

.product-image {
  width: 40px;
  height: 40px;
  border-radius: 4px;
  overflow: hidden;
}

.product-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.product-name {
  color: #333;
  font-weight: 500;
}

.progress-bar {
  width: 100%;
  height: 8px;
  background: #f0f0f0;
  border-radius: 4px;
  margin-bottom: 5px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  background: #3498db;
  border-radius: 4px;
  transition: width 0.3s;
}

.percentage {
  font-size: 12px;
  color: #666;
  font-weight: 500;
}

/* 用户行为分析 */
.user-behavior {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 30px;
}

.behavior-item {
  text-align: center;
}

.behavior-item h4 {
  margin: 0 0 20px 0;
  color: #333;
  font-size: 16px;
}

.pie-chart {
  height: 200px;
  position: relative;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .analytics-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 10px;
  }
  
  .stats-overview {
    grid-template-columns: 1fr;
  }
  
  .user-behavior {
    grid-template-columns: 1fr;
  }
}
</style>