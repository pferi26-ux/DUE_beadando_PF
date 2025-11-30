import requests

URL = "http://127.0.0.1:5000"

class ServiceClient:

    def pf_list_intervals(self):
        response = requests.get(f"{URL}/intervals")
        return response.json()

    def pf_add_interval(self, vehicle: str, owner: str, interval_km: int):
        data = {
            "vehicle": vehicle,
            "owner": owner,
            "interval_km": interval_km
        }
        response = requests.post(f"{URL}/intervals", json=data)
        return response.json()

    def pf_mod_interval(self, interval_id: int, interval_km: int):
        data = {
            "interval_id": interval_id,
            "interval_km": interval_km
        }
        response = requests.post(f"{URL}/intervals/{interval_id}", json=data)
        return response.json()

    def pf_delete_interval(self, interval_id: int):
        response = requests.delete(f"{URL}/intervals/{interval_id}")
        return response.json()

if __name__ == "__main__":
    client = ServiceClient()
