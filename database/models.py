# database/models.py
from datetime import datetime, timedelta
import hashlib

class SubscriptionManager:
    """Управление подписками"""
    
    @staticmethod
    def check_device_limit(current_devices, max_devices=2):
        """Проверяет лимит устройств"""
        return current_devices < max_devices
    
    @staticmethod
    def get_device_info(user_agent):
        """Определяет информацию об устройстве"""
        ua = user_agent.lower()
        
        if 'iphone' in ua:
            return 'iPhone', 'ios'
        elif 'ipad' in ua:
            return 'iPad', 'ios'
        elif 'android' in ua:
            if 'mobile' in ua:
                return 'Android Phone', 'android'
            else:
                return 'Android Tablet', 'android'
        elif 'windows' in ua:
            return 'Windows PC', 'windows'
        elif 'mac' in ua:
            return 'Mac', 'macos'
        elif 'linux' in ua:
            return 'Linux', 'linux'
        else:
            return 'Unknown Device', 'unknown'
    
    @staticmethod
    def format_expiry_date(expires_at):
        """Форматирует дату истечения"""
        if not expires_at:
            return None
        
        now = datetime.now()
        delta = expires_at - now
        
        if delta.days > 0:
            return f"{delta.days} дней"
        elif delta.seconds > 3600:
            hours = delta.seconds // 3600
            return f"{hours} часов"
        else:
            minutes = delta.seconds // 60
            return f"{minutes} минут"
