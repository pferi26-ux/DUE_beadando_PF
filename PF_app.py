from flask import Flask, request, jsonify
from PF_database import init_db, get_connection
app = Flask(__name__)

init_db()

class ServiceInterval:
    def __init__(self, vehicle: str, owner: str, interval_km: int, sid: int = None):
        self.id = sid
        self.vehicle = vehicle
        self.owner = owner
        self.interval_km = interval_km

@app.route("/intervals", methods=["GET"])
def pf_list_intervals():
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT id, vehicle, owner, interval_km FROM intervals")
    rows = c.fetchall()
    conn.close()

    return jsonify([
        {"id": r[0], "vehicle": r[1], "owner": r[2], "interval_km": r[3]}
        for r in rows
    ])

@app.route("/intervals", methods=["POST"])
def pf_add_interval():
    data = request.json
    interval = ServiceInterval(
        vehicle=data["vehicle"],
        owner=data["owner"],
        interval_km=data["interval_km"]
    )
    conn = get_connection()
    c = conn.cursor()
    c.execute(
        "INSERT INTO intervals (vehicle, owner, interval_km) VALUES (?, ?, ?)",
        (interval.vehicle, interval.owner, interval.interval_km)
    )
    conn.commit()
    conn.close()

    return jsonify({"status": "ok"}), 201

@app.route("/intervals/<int:sid>", methods=["POST"])
def pf_mod_interval(sid):
    data = request.json
    mod_km=data["interval_km"]

    conn = get_connection()
    c = conn.cursor()
    c.execute(
        "UPDATE intervals SET interval_km=? WHERE id = ?",
        (mod_km,sid)
    )
    conn.commit()
    conn.close()

    return jsonify({"status": "ok"}), 201

@app.route("/intervals/<int:sid>", methods=["DELETE"])
def pf_delete_interval(sid):
    conn = get_connection()
    c = conn.cursor()
    c.execute(
        "DELETE FROM intervals WHERE id = ?",
        (sid,)
    )
    conn.commit()
    conn.close()

    return jsonify({"status": "deleted"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
