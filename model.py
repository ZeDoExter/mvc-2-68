import json
import os
from datetime import datetime

DB_FILE = 'database.json'

def init_db():
    """สร้างไฟล์ JSON ถ้ายังไม่มี"""
    if not os.path.exists(DB_FILE):
        data = {
            'shelters': [
                {'id': 'S001', 'name': 'ศูนย์ตัวเมือง', 'capacity': 4, 'risk': 'low', 'current': 0},
                {'id': 'S002', 'name': 'ศูนย์ชื่นชัย', 'capacity': 6, 'risk': 'medium', 'current': 0},
                {'id': 'S003', 'name': 'ศูนย์นครสวรรค์', 'capacity': 5, 'risk': 'high', 'current': 0},
                {'id': 'S004', 'name': 'ศูนย์เฉลิม', 'capacity': 3, 'risk': 'low', 'current': 0},
                {'id': 'S005', 'name': 'ศูนย์สมเด็จ', 'capacity': 7, 'risk': 'medium', 'current': 0},
            ],
            'citizens': [
                # VIP 5 คน
                {'id': 'C001', 'name': 'นายสุชัย สมิทธิ', 'age': 55, 'health': 'healthy', 'type': 'vip', 'assigned': False},
                {'id': 'C002', 'name': 'นางสมเด็จ ใจสงค์', 'age': 70, 'health': 'at_risk', 'type': 'vip', 'assigned': False},
                {'id': 'C003', 'name': 'นายวิทยา เรืองสว่าง', 'age': 8, 'health': 'healthy', 'type': 'vip', 'assigned': False},
                {'id': 'C004', 'name': 'นางปิยพัฒน์ บูรพ', 'age': 50, 'health': 'healthy', 'type': 'vip', 'assigned': False},
                {'id': 'C005', 'name': 'นายอนุชิต สิงห์', 'age': 62, 'health': 'at_risk', 'type': 'vip', 'assigned': False},
                # กลุ่มเสี่ยง 12 คน (เด็ก + ผู้สูงอายุ)
                {'id': 'C006', 'name': 'น้อย สมชาย', 'age': 8, 'health': 'healthy', 'type': 'risk_group', 'assigned': False},
                {'id': 'C007', 'name': 'เนม สุชีร์', 'age': 10, 'health': 'healthy', 'type': 'risk_group', 'assigned': False},
                {'id': 'C008', 'name': 'หนึ่ง จริยา', 'age': 5, 'health': 'at_risk', 'type': 'risk_group', 'assigned': False},
                {'id': 'C009', 'name': 'สอง ศิริพัฒน์', 'age': 9, 'health': 'healthy', 'type': 'risk_group', 'assigned': False},
                {'id': 'C010', 'name': 'ยายแจม ประสิทธิ', 'age': 72, 'health': 'at_risk', 'type': 'risk_group', 'assigned': False},
                {'id': 'C011', 'name': 'ปู่สุมิตร พิพัฒน์', 'age': 68, 'health': 'healthy', 'type': 'risk_group', 'assigned': False},
                {'id': 'C012', 'name': 'ยายวิไล เสนา', 'age': 65, 'health': 'at_risk', 'type': 'risk_group', 'assigned': False},
                {'id': 'C013', 'name': 'ปู่คำชัย กำธร', 'age': 70, 'health': 'healthy', 'type': 'risk_group', 'assigned': False},
                {'id': 'C014', 'name': 'น้ำหนึ่ง กิตติ', 'age': 7, 'health': 'healthy', 'type': 'risk_group', 'assigned': False},
                {'id': 'C015', 'name': 'ยายมณฑา อินทร์', 'age': 64, 'health': 'healthy', 'type': 'risk_group', 'assigned': False},
                {'id': 'C016', 'name': 'ปู่มิ่ง วิจารณ์', 'age': 75, 'health': 'at_risk', 'type': 'risk_group', 'assigned': False},
                {'id': 'C017', 'name': 'ออม ศรีภา', 'age': 11, 'health': 'at_risk', 'type': 'risk_group', 'assigned': False},
                # ทั่วไป 13 คน
                {'id': 'C018', 'name': 'สมชาย ใจดี', 'age': 25, 'health': 'healthy', 'type': 'normal', 'assigned': False},
                {'id': 'C019', 'name': 'อรพิณ รัตนา', 'age': 30, 'health': 'healthy', 'type': 'normal', 'assigned': False},
                {'id': 'C020', 'name': 'สมศักดิ์ อภิมาน', 'age': 28, 'health': 'at_risk', 'type': 'normal', 'assigned': False},
                {'id': 'C021', 'name': 'นรินทร์ สิงห์', 'age': 35, 'health': 'healthy', 'type': 'normal', 'assigned': False},
                {'id': 'C022', 'name': 'จารุวรรณ ไชยสิทธิ', 'age': 26, 'health': 'healthy', 'type': 'normal', 'assigned': False},
                {'id': 'C023', 'name': 'วิชัย อมรสิทธิ', 'age': 40, 'health': 'healthy', 'type': 'normal', 'assigned': False},
                {'id': 'C024', 'name': 'พรชนก เฉิดฉาย', 'age': 32, 'health': 'at_risk', 'type': 'normal', 'assigned': False},
                {'id': 'C025', 'name': 'ธวัฒน์ ศรีศร', 'age': 29, 'health': 'healthy', 'type': 'normal', 'assigned': False},
                {'id': 'C026', 'name': 'ประพัฒน์ นาคนิคม', 'age': 42, 'health': 'healthy', 'type': 'normal', 'assigned': False},
                {'id': 'C027', 'name': 'สิรินญา บวรพร', 'age': 27, 'health': 'healthy', 'type': 'normal', 'assigned': False},
                {'id': 'C028', 'name': 'ชัยพร สัทธาพร', 'age': 38, 'health': 'at_risk', 'type': 'normal', 'assigned': False},
                {'id': 'C029', 'name': 'ภัคจรา อมรผล', 'age': 24, 'health': 'healthy', 'type': 'normal', 'assigned': False},
                {'id': 'C030', 'name': 'กมล ชิมพลา', 'age': 36, 'health': 'healthy', 'type': 'normal', 'assigned': False},
            ],
            'assignments': []
        }
        with open(DB_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

def load():
    """โหลดข้อมูล"""
    with open(DB_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save(data):
    """บันทึกข้อมูล"""
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def get_shelters():
    """ดึงศูนย์พักพิงทั้งหมด"""
    return load()['shelters']

def get_citizens():
    """ดึงประชาชนทั้งหมด"""
    return load()['citizens']

def get_assignments():
    """ดึงการจัดสรรทั้งหมด"""
    return load()['assignments']

def add_citizen(citizen_id, name, age, health, ctype):
    """เพิ่มประชาชน"""
    data = load()
    data['citizens'].append({
        'id': citizen_id,
        'name': name,
        'age': age,
        'health': health,
        'type': ctype,
        'assigned': False
    })
    save(data)

def citizen_exists(citizen_id):
    """เช็คว่าประชาชนมีแล้วหรือไม่"""
    data = load()
    return any(c['id'] == citizen_id for c in data['citizens'])

def allocate():
    """จัดสรรประชาชนไปยังศูนย์พักพิง"""
    data = load()
    
    # เรียงลำดับ: VIP > risk_group > normal และ เด็ก/ผู้สูงอายุก่อน
    citizens = [c for c in data['citizens'] if not c['assigned']]
    citizens.sort(key=lambda c: (
        0 if c['type'] == 'vip' else (1 if c['type'] == 'risk_group' else 2),
        0 if c['age'] < 12 or c['age'] >= 60 else 1
    ))
    
    for citizen in citizens:
        # หาศูนย์ที่เหมาะสม
        shelters = data['shelters']
        
        # ถ้าสุขภาพเสี่ยง ต้องไปศูนย์ risk = 'low'
        if citizen['health'] == 'at_risk':
            available = [s for s in shelters if s['risk'] == 'low' and s['current'] < s['capacity']]
        else:
            available = [s for s in shelters if s['current'] < s['capacity']]
        
        if available:
            # เลือกศูนย์ที่มีที่ว่างมากสุด
            best = max(available, key=lambda s: s['capacity'] - s['current'])
            
            # จัดสรร
            data['assignments'].append({
                'citizen_id': citizen['id'],
                'citizen_name': citizen['name'],
                'shelter_id': best['id'],
                'shelter_name': best['name'],
                'date': datetime.now().strftime('%Y-%m-%d %H:%M')
            })
            
            # อัปเดต
            for c in data['citizens']:
                if c['id'] == citizen['id']:
                    c['assigned'] = True
            
            for s in data['shelters']:
                if s['id'] == best['id']:
                    s['current'] += 1
    
    save(data)
