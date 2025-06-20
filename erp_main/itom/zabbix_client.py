import os
import requests
from typing import Any, Dict, List

from django.conf import settings


class ZabbixClient:
    """Minimal client for Zabbix API."""

    def __init__(self):
        self.url = settings.ZABBIX_URL.rstrip('/') + '/api_jsonrpc.php'
        self.user = settings.ZABBIX_USER
        self.password = settings.ZABBIX_PASSWORD
        self.auth_token: str | None = None
        if self.user and self.password:
            self.login()

    def _request(self, method: str, params: Dict[str, Any] | None = None) -> Any:
        payload = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params or {},
            "auth": self.auth_token,
            "id": 1,
        }
        response = requests.post(self.url, json=payload, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("result")

    def login(self) -> None:
        result = self._request(
            "user.login",
            {"user": self.user, "password": self.password},
        )
        self.auth_token = result

    # Example API wrappers -------------------------------------------------
    def get_hosts(self) -> List[Dict[str, Any]]:
        return self._request("host.get", {"output": ["hostid", "host"]})

    def create_host(self, host: str, ip: str) -> Any:
        params = {
            "host": host,
            "interfaces": [
                {
                    "type": 1,
                    "main": 1,
                    "useip": 1,
                    "ip": ip,
                    "dns": "",
                    "port": "10050",
                }
            ],
            "groups": [{"groupid": "2"}],
        }
        return self._request("host.create", params)

    def host_status_summary(self) -> Any:
        hosts = self._request("host.get", {"output": ["hostid", "name", "status"]})
        return hosts
