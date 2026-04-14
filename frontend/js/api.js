// API Configuration
const API_BASE_URL = 'http://localhost:5000/api';

// API Helper Functions
const API = {
    // Generic GET request
    async get(endpoint) {
        try {
            const response = await fetch(`${API_BASE_URL}${endpoint}`);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return await response.json();
        } catch (error) {
            console.error(`API GET Error (${endpoint}):`, error);
            throw error;
        }
    },

    // Generic POST request
    async post(endpoint, data) {
        try {
            const response = await fetch(`${API_BASE_URL}${endpoint}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            });
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return await response.json();
        } catch (error) {
            console.error(`API POST Error (${endpoint}):`, error);
            throw error;
        }
    },

    // Specific API endpoints
    loadData() {
        return this.get('/load-data');
    },

    getStats() {
        return this.get('/stats');
    },

    getGeoAnalysis() {
        return this.get('/geo-analysis');
    },

    getLoginLogs(filters = {}) {
        const params = new URLSearchParams(filters);
        return this.get(`/login-logs?${params}`);
    },

    checkBloom(ip) {
        return this.post('/bloom-check', { ip });
    },

    getAnomalyDetection() {
        return this.get('/anomaly-detect');
    },

    getRecentAlerts() {
        return this.get('/recent-alerts');
    },

    getTimeline() {
        return this.get('/timeline');
    },

    getUserAnalysis(username) {
        return this.get(`/user-analysis/${username}`);
    }
};

// Utility Functions
function showLoading(elementId) {
    const element = document.getElementById(elementId);
    if (element) {
        element.innerHTML = `
            <div class="loading">
                <div class="spinner"></div>
                <p>Loading data...</p>
            </div>
        `;
    }
}

function showError(elementId, message) {
    const element = document.getElementById(elementId);
    if (element) {
        element.innerHTML = `
            <div class="alert-item critical">
                <div class="alert-content">
                    <h4>Error</h4>
                    <p>${message}</p>
                </div>
            </div>
        `;
    }
}

function formatNumber(num) {
    return num.toLocaleString();
}

function formatTimestamp(timestamp) {
    const date = new Date(timestamp);
    return date.toLocaleString();
}

// Export for use in other files
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { API, showLoading, showError, formatNumber, formatTimestamp };
}
