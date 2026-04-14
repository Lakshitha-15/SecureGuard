import pandas as pd

class GeoAnalyzer:
    """
    Geographic Analysis for login data
    Provides insights about login patterns across different countries and cities
    """
    
    def __init__(self, df):
        """Initialize with login data"""
        self.df = df
    
    def get_country_stats(self):
        """Get statistics by country"""
        country_stats = []
        
        for country in self.df['country'].unique():
            country_df = self.df[self.df['country'] == country]
            
            total = len(country_df)
            failed = len(country_df[country_df['status'] == 'failed'])
            success = len(country_df[country_df['status'] == 'success'])
            
            country_stats.append({
                'country': country,
                'total_logins': total,
                'success_logins': success,
                'failed_logins': failed,
                'success_rate': round((success / total) * 100, 2) if total > 0 else 0,
                'unique_users': country_df['username'].nunique()
            })
        
        # Sort by total logins
        country_stats = sorted(country_stats, key=lambda x: x['total_logins'], reverse=True)
        
        return country_stats
    
    def get_city_stats(self):
        """Get statistics by city"""
        city_stats = []
        
        city_groups = self.df.groupby(['country', 'city']).agg({
            'username': 'count',
            'status': lambda x: (x == 'success').sum()
        }).reset_index()
        
        city_groups.columns = ['country', 'city', 'total', 'success']
        city_groups['failed'] = city_groups['total'] - city_groups['success']
        
        for _, row in city_groups.iterrows():
            city_stats.append({
                'country': row['country'],
                'city': row['city'],
                'total_logins': int(row['total']),
                'success_logins': int(row['success']),
                'failed_logins': int(row['failed'])
            })
        
        # Sort by total logins
        city_stats = sorted(city_stats, key=lambda x: x['total_logins'], reverse=True)
        
        return city_stats[:20]  # Top 20 cities
    
    def get_country_distribution(self):
        """Get login distribution by country for charts"""
        country_counts = self.df['country'].value_counts()
        
        return {
            'countries': country_counts.index.tolist(),
            'counts': country_counts.values.tolist()
        }
    
    def get_status_by_country(self):
        """Get success/failed distribution by country"""
        result = {}
        
        for country in self.df['country'].unique():
            country_df = self.df[self.df['country'] == country]
            status_counts = country_df['status'].value_counts().to_dict()
            
            result[country] = {
                'success': status_counts.get('success', 0),
                'failed': status_counts.get('failed', 0)
            }
        
        return result
    
    def get_top_countries(self, limit=10):
        """Get top countries by login count"""
        country_counts = self.df['country'].value_counts().head(limit)
        
        return {
            'countries': country_counts.index.tolist(),
            'counts': country_counts.values.tolist()
        }
    
    def get_map_data(self):
        """Get data formatted for map visualization"""
        map_data = []
        
        country_groups = self.df.groupby('country').agg({
            'username': 'count',
            'status': lambda x: (x == 'success').sum()
        }).reset_index()
        
        country_groups.columns = ['country', 'total', 'success']
        country_groups['failed'] = country_groups['total'] - country_groups['success']
        
        for _, row in country_groups.iterrows():
            map_data.append({
                'country': row['country'],
                'total': int(row['total']),
                'success': int(row['success']),
                'failed': int(row['failed']),
                'success_rate': round((row['success'] / row['total']) * 100, 2)
            })
        
        return map_data
    
    def get_analysis(self):
        """Get complete geographic analysis"""
        return {
            'country_stats': self.get_country_stats(),
            'city_stats': self.get_city_stats(),
            'country_distribution': self.get_country_distribution(),
            'status_by_country': self.get_status_by_country(),
            'top_countries': self.get_top_countries(),
            'map_data': self.get_map_data()
        }
