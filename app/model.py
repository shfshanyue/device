from . import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

    def __repr__(self):
        return '<User {!r}>'.format(self.name)

class EquipmentShutdown(db.Model):
    __tablename__ = 'shutdown'

    id = db.Column(db.Integer, primary_key=True)
    equipment_number = db.Column(db.Integer)
    stoping_date = db.Column(db.Date)
    recovery_date = db.Column(db.Date)
    downtime_reason = db.Column(db.Text)
    remarks = db.Column(db.Text)

    def __repr__(self):
        return '<EquipmentShutdown {!r}>'.format(self.name)

class EquipmentError(db.Model):
    __tablename__ = 'equipment_error'

    id = db.Column(db.Integer, primary_key=True)
    equipment_number = db.Column(db.Integer)
    equipment_name = db.Column(db.String(128))
    deparentment = db.Column(db.String(128))
    responsible_person = db.Column(db.String(128))
    fault_location = db.Column(db.String(128))
    fault_type = db.Column(db.String(128))
    fault_date = db.Column(db.DateTime)
    maintenance_time = db.Column(db.DateTime)
    maintenance_costs = db.Column(db.Float)
    failure_phenomena = db.Column(db.String(128))
    repaire_person = db.Column(db.Text)
    solution = db.Column(db.Text)

    def __repr__(self):
        return '<EquipmentError {!r}>'.format(self.name)

class EquipmentRepair(db.Model):
    __tablename__ = 'equipment_repair'

    id = db.Column(db.Integer, primary_key=True)
    equipment_number = db.Column(db.Integer)
    stop_date = db.Column(db.DateTime)
    recovery_date = db.Column(db.DateTime)
    repaire_person = db.Column(db.String(128))
    approved_person = db.Column(db.String(128))
    maintenance_costs = db.Column(db.Float)
    spare_equipment_number = db.Column(db.Integer)
    use_material = db.Column(db.String(128))
    tool = db.Column(db.String(128))
    remarks = db.Column(db.Text)

    def __repr__(self):
        return '<EquipmentRepair {!r}>'.format(self.name)

class EquipmentRecord(db.Model):
    __tablename__ = 'equipment_record'

    id = db.Column(db.Integer, primary_key=True)
    equipment_number = db.Column(db.Integer)
    record_time = db.Column(db.DateTime)
    note_taker = db.Column(db.String(128))
    title = db.Column(db.String(128))
    content = db.Column(db.Text)

class EquipmentMain(db.Model):
    __tablename__ = 'equiment_main'

    id = db.Column(db.Integer, primary_key=True)
    equipment_number = db.Column(db.Integer)
    equipment_name = db.Column(db.String(128))
    department = db.Column(db.String(128))
    maintenance_time = db.Column(db.DateTime)
    maintenance_period = db.Column(db.String(128))
    maintenance_estimated_cost = db.Column(db.Float)
    maintenance_content = db.Column(db.Text)
    maintenance_standards = db.Column(db.Text)
    maintenance_responsible_person = db.Column(db.String(128))

class EquipmentFaultPeriod(db.Model):
    __tablename__ = 'equiment_fault_period'

    id = db.Column(db.Integer, primary_key=True)
    equipment_number = db.Column(db.Integer)
    fault_type = db.Column(db.String(128))
    expected_period = db.Column(db.String(128))
    recent_failure_date = db.Column(db.DateTime)
    expected_date = db.Column(db.DateTime)
    remarks = db.Column(db.Text)

class EquipmentInfo(db.Model):
    __tablename__ = 'equiment_info'

    id = db.Column(db.Integer, primary_key=True)
    equipment_number = db.Column(db.Integer)
    equipment_name = db.Column(db.String(128))
    department = db.Column(db.String(128))
    equipment_type = db.Column(db.String(128))
    equipment_model = db.Column(db.String(128))
    equipment_status = db.Column(db.String(128))
    use_time = db.Column(db.DateTime)
    date_of_production = db.Column(db.DateTime)
    date_of_retirement = db.Column(db.DateTime)
    ex_factory_price = db.Column(db.Float)
    code_section = db.Column(db.Text)
    remarks = db.Column(db.Text)

class EquipmentAnaly(db.Model):
    __tablename__ = 'equiment_analy'

    id = db.Column(db.Integer, primary_key=True)
    equipment_number = db.Column(db.Integer)
    equipment_names = db.Column(db.String)
    department = db.Column(db.String)
    responsible_person = db.Column(db.String)
    alarm_frequency = db.Column(db.String)
    rated_current = db.Column(db.String)
    rated_voltage = db.Column(db.String)



