import model

def register_citizen(citizen_id, name, age, health, ctype):
    if model.citizen_exists(citizen_id):
        return {'success': False, 'message': 'รหัสนี้ลงทะเบียนแล้ว'}
    
    model.add_citizen(citizen_id, name, age, health, ctype)
    return {'success': True, 'message': 'ลงทะเบียนสำเร็จ'}

def get_all_citizens():
    return model.get_citizens()

def get_citizens_by_type(ctype):
    all_citizens = model.get_citizens()
    return [c for c in all_citizens if c['type'] == ctype]

def get_shelters():
    return model.get_shelters()

def allocate_citizens():
    model.allocate()

def get_report():
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
