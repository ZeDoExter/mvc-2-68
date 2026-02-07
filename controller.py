import model

def register_citizen(citizen_id, name, age, health, ctype):
    """ลงทะเบียนประชาชน"""
    if model.citizen_exists(citizen_id):
        return {'success': False, 'message': 'รหัสนี้ลงทะเบียนแล้ว'}
    
    model.add_citizen(citizen_id, name, age, health, ctype)
    return {'success': True, 'message': 'ลงทะเบียนสำเร็จ'}

def get_all_citizens():
    """ดึงประชาชนทั้งหมด"""
    return model.get_citizens()

def get_citizens_by_type(ctype):
    """ดึงประชาชนตามประเภท"""
    all_citizens = model.get_citizens()
    return [c for c in all_citizens if c['type'] == ctype]

def get_shelters():
    """ดึงศูนย์พักพิงทั้งหมด"""
    return model.get_shelters()

def allocate_citizens():
    """จัดสรรประชาชน"""
    model.allocate()

def get_report():
    """สรุปรายงาน"""
    citizens = model.get_citizens()
    assignments = model.get_assignments()
    
    assigned = [c for c in citizens if c['assigned']]
    unassigned = [c for c in citizens if not c['assigned']]
    
    return {
        'assigned': assigned,
        'unassigned': unassigned,
        'assignments': assignments,
        'total': len(citizens)
    }
