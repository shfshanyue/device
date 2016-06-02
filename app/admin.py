# coding: utf-8

from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView

from .model import User, EquipmentShutdown, EquipmentError, EquipmentRepair, EquipmentRecord, EquipmentMain, EquipmentFaultPeriod, EquipmentInfo, EquipmentAnaly

from . import db

admin = Admin(name=u'化机生产装备故障信息分析与数据库管理系统', template_mode='bootstrap3')


class ShutDownView(ModelView):
    _labels = (u'设备编号', u'停机日期', u'恢复日期', u'停机原因', u'备注')
    _columns = ('equipment_number', 'stoping_date', 'recovery_date', 'downtime_reason', 'remarks')
    column_labels = dict(zip(_columns, _labels))


class ErrorView(ModelView):
    _labels = (u'设备编号', u'设备名称', u'所属部门', u'设备负责', u'故障部位', u'故障类型', u'故障发生时间', u'维修时间', u'维修费用', u'故障现象', u'维修人员', u'故障原因', u'解决方案')
    _columns = ('equipment_number', 'equipment_name', 'deparentment', 'responsible_person', 'fault_location', 'fault_type', 'fault_date', 'maintenance_time', 'maintenance_costs', 'failure_phenomena', 'repaire_person', 'solution')
    column_labels = dict(zip(_columns, _labels))


class RepairView(ModelView):
    _labels = (u'设备编号', '停机日期', u'恢复日期', u'维修人员', u'批准人', u'维修费用', u'备用设备编号', u'使用材料', u'使用工具', u'备注')
    _columns = ('equipment_number', 'stop_date', 'recovery_date', 'repaire_person', 'approved_person', 'maintenance_costs', 'spare_equipment_number', 'use_material', 'tool', 'remarks')
    column_labels = dict(zip(_columns, _labels))

class RecordView(ModelView):
    _labels = (u'设备编号', u'记录时间', u'记录人', u'标题', u'内容')
    _columns = ('equipment_number', 'record_time', 'note_taker', 'title', 'content')
    column_labels = dict(zip(_columns, _labels))


class MainView(ModelView):
    _labels = (u'设备编号', u'设备名称', u'所属部门', u'保养时间', u'保养周期', u'保养预计费用', u'保养内容', u'保养标准', u'保养负责人')
    _columns = ('equipment_number', 'equipment_name', 'department', 'maintenance_time', 'maintenance_period', 'maintenance_estimated_cost', 'maintenance_content', 'maintenance_standards', 'maintenance_responsible_person')
    column_labels = dict(zip(_columns, _labels))


class FaultView(ModelView):
    _labels = (u'设备编号', u'故障类型', u'预计周期', u'最近故障日期', u'预计故障日期', u'备注')
    _columns = ('equipment_number', 'fault_type', 'expected_period', 'recent_failure_date', 'expected_date', 'remarks')
    column_labels = dict(zip(_columns, _labels))


class InfoView(ModelView):
    _labels = (u'设备编号', u'设备名称', u'所属部门', u'设备类型', u'设备型号', u'设备状态', u'使用时间', u'出厂日期', u'报废日期', u'出厂价钱', u'工段代码', u'备注')
    _columns = ('equipment_number', 'equipment_name', 'department', 'equipment_type', 'equipment_model', 'equipment_status', 'use_time', 'date_of_production', 'date_of_retirement', 'ex_factory_price', 'code_section', 'remarks')
    column_labels = dict(zip( _columns, _labels))

class AnalyView(ModelView):
    _columns = ('equipment_number', 'equipment_names', 'department', 'responsible_person', 'alarm_frequency', 'rated_current', 'rated_voltage')
    _labels = (
        u'设备编号', u'设备名称', u'所属部门', u'设备负责人', u'报警次数', u'额定电流', u'额定电压')
    column_labels = dict(zip(_columns, _labels))


admin.add_view(InfoView(EquipmentInfo, db.session, name=u'基本信息'))
admin.add_view(RecordView(EquipmentRecord, db.session, name=u'工作记录'))
admin.add_view(MainView(EquipmentMain, db.session, name=u'保养记录'))
admin.add_view(ErrorView(EquipmentError, db.session, name=u'故障记录'))
admin.add_view(FaultView(EquipmentFaultPeriod, db.session, name=u'故障周期记录'))
admin.add_view(ShutDownView(EquipmentShutdown, db.session, name=u'停机记录'))
admin.add_view(RepairView(EquipmentRepair, db.session, name=u'维修记录'))
admin.add_view(AnalyView(EquipmentAnaly, db.session, name=u'分析记录'))
