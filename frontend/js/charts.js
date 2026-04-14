// Chart.js Configuration and Utilities

// Default Chart Options
const defaultChartOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
        legend: {
            labels: {
                color: '#cbd5e1'
            }
        }
    },
    scales: {
        x: {
            ticks: { color: '#cbd5e1' },
            grid: { color: 'rgba(51, 65, 85, 0.5)' }
        },
        y: {
            ticks: { color: '#cbd5e1' },
            grid: { color: 'rgba(51, 65, 85, 0.5)' }
        }
    }
};

// Chart Colors
const chartColors = {
    primary: '#6366f1',
    success: '#10b981',
    danger: '#ef4444',
    warning: '#f59e0b',
    info: '#3b82f6',
    purple: '#8b5cf6',
    pink: '#ec4899',
    cyan: '#06b6d4'
};

// Create Bar Chart
function createBarChart(canvasId, labels, data, label = 'Data') {
    const ctx = document.getElementById(canvasId);
    if (!ctx) return null;

    return new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: label,
                data: data,
                backgroundColor: chartColors.primary,
                borderColor: chartColors.primary,
                borderWidth: 1
            }]
        },
        options: {
            ...defaultChartOptions,
            plugins: {
                ...defaultChartOptions.plugins,
                title: {
                    display: false
                }
            }
        }
    });
}

// Create Pie Chart
function createPieChart(canvasId, labels, data) {
    const ctx = document.getElementById(canvasId);
    if (!ctx) return null;

    return new Chart(ctx, {
        type: 'pie',
        data: {
            labels: labels,
            datasets: [{
                data: data,
                backgroundColor: [
                    chartColors.success,
                    chartColors.danger,
                    chartColors.warning,
                    chartColors.info,
                    chartColors.purple
                ]
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        color: '#cbd5e1',
                        padding: 15
                    }
                }
            }
        }
    });
}

// Create Line Chart
function createLineChart(canvasId, labels, datasets) {
    const ctx = document.getElementById(canvasId);
    if (!ctx) return null;

    return new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: datasets
        },
        options: {
            ...defaultChartOptions,
            plugins: {
                ...defaultChartOptions.plugins,
                title: {
                    display: false
                }
            }
        }
    });
}

// Create Doughnut Chart
function createDoughnutChart(canvasId, labels, data) {
    const ctx = document.getElementById(canvasId);
    if (!ctx) return null;

    return new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: labels,
            datasets: [{
                data: data,
                backgroundColor: [
                    chartColors.primary,
                    chartColors.success,
                    chartColors.danger,
                    chartColors.warning,
                    chartColors.info
                ]
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'right',
                    labels: {
                        color: '#cbd5e1',
                        padding: 10
                    }
                }
            }
        }
    });
}

// Create Multi-Dataset Line Chart
function createMultiLineChart(canvasId, labels, successData, failedData) {
    const ctx = document.getElementById(canvasId);
    if (!ctx) return null;

    return new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [
                {
                    label: 'Success',
                    data: successData,
                    borderColor: chartColors.success,
                    backgroundColor: 'rgba(16, 185, 129, 0.1)',
                    tension: 0.4,
                    fill: true
                },
                {
                    label: 'Failed',
                    data: failedData,
                    borderColor: chartColors.danger,
                    backgroundColor: 'rgba(239, 68, 68, 0.1)',
                    tension: 0.4,
                    fill: true
                }
            ]
        },
        options: defaultChartOptions
    });
}

// Destroy chart if exists
function destroyChart(chart) {
    if (chart) {
        chart.destroy();
    }
}

// Export functions
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        createBarChart,
        createPieChart,
        createLineChart,
        createDoughnutChart,
        createMultiLineChart,
        destroyChart,
        chartColors
    };
}
