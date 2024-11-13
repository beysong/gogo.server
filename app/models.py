

from . import db
from sqlalchemy.sql import func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import func, Boolean, DateTime, Integer, String, Date, ForeignKey

# 定义通用基类
class Base(DeclarativeBase):
    __abstract__ = True  # 声明为抽象基类，不能直接实例化

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime, onupdate=func.now())
    is_delete: Mapped[bool] = mapped_column(Boolean, default=False)


# 将通用基类与 SQLAlchemy 关联
Base.metadata = db.metadata


class User(Base):
    
    name: Mapped[str] = mapped_column(String(20))
    username: Mapped[str] = mapped_column(String(20))
    password_hash: Mapped[str] = mapped_column(String(128))

    def __repr__(self):
        return f"<User id={self.id}, name={self.name}, created_at={self.created_at}, updated_at={self.updated_at}, is_delete={self.is_delete}>"



class Employee(Base):
    __tablename__ = 'employees'
    
    out_id: Mapped[str] = mapped_column(String(50), unique=True)  # 外部工号
    tax_id: Mapped[str] = mapped_column(String(50), unique=True)  # 税务编号
    hire_date: Mapped[Date] = mapped_column(Date)  # 入职日期
    department: Mapped[str] = mapped_column(String(100))  # 部门
    cost_center: Mapped[str] = mapped_column(String(100))  # 成本中心
    name: Mapped[str] = mapped_column(String(100))  # 姓名
    resignation_date: Mapped[Date] = mapped_column(Date)  # 离职日期
    position: Mapped[str] = mapped_column(String(100))  # 职务
    id_card_number: Mapped[str] = mapped_column(String(50))  # 身份证号
    bank_name: Mapped[str] = mapped_column(String(100))  # 银行名称
    bank_card_number: Mapped[str] = mapped_column(String(50))  # 卡号
    fixed_salary: Mapped[int] = mapped_column(Integer)  # 固定工资
    performance_bonus: Mapped[int] = mapped_column(Integer)  # 绩效奖金
    
    seniority_award: Mapped[int] = mapped_column(Integer)  # 工龄奖 是否有 boolean
    meal_subsidy: Mapped[int] = mapped_column(Integer)  # 餐补 是否有 boolean
    travel_allowance: Mapped[int] = mapped_column(Integer)  # 出差津贴 是否有 boolean
    comprehensive_subsidy: Mapped[int] = mapped_column(Integer)  # 综合补贴 是否有 boolean
    other_subsidy: Mapped[int] = mapped_column(Integer)  # 其他津贴 是否有 boolean
    performance_rating: Mapped[str] = mapped_column(String(50))  # 评比绩效 是否有 boolean

    # 关系
    salaries: Mapped[list["Salary"]] = relationship(back_populates="employee")
    
    
class Salary(Base):
    __tablename__ = 'salaries'
    
    employee_id: Mapped[int] = mapped_column(ForeignKey('employees.id'))  # 关联员工表的外键
    month: Mapped[Date] = mapped_column(Date)  # 工资月份
    out_id: Mapped[str] = mapped_column(String(50), unique=True)  # 外部工号
    tax_id: Mapped[str] = mapped_column(String(50), unique=True)  # 税务编号
    hire_date: Mapped[Date] = mapped_column(Date)  # 入职日期
    department: Mapped[str] = mapped_column(String(100))  # 部门
    cost_center: Mapped[str] = mapped_column(String(100))  # 成本中心
    name: Mapped[str] = mapped_column(String(100))  # 姓名
    resignation_date: Mapped[Date] = mapped_column(Date)  # 离职日期
    position: Mapped[str] = mapped_column(String(100))  # 职务
    id_card_number: Mapped[str] = mapped_column(String(50))  # 身份证号
    bank_name: Mapped[str] = mapped_column(String(100))  # 银行名称
    bank_card_number: Mapped[str] = mapped_column(String(50))  # 卡号

    attendance_status: Mapped[str] = mapped_column(String(50))  # 出勤状况
    actual_attendance_days: Mapped[int] = mapped_column(Integer)  # 实际出勤天数
    personal_leave_hours: Mapped[int] = mapped_column(Integer)  # 事假工时
    sick_leave_hours: Mapped[int] = mapped_column(Integer)  # 病假工时
    fixed_salary: Mapped[int] = mapped_column(Integer)  # 固定工资
    performance_bonus: Mapped[int] = mapped_column(Integer)  # 绩效奖金
    total_salary: Mapped[int] = mapped_column(Integer)  # 工资合计
    seniority_award: Mapped[int] = mapped_column(Integer)  # 工龄奖
    meal_subsidy: Mapped[int] = mapped_column(Integer)  # 餐补
    travel_allowance: Mapped[int] = mapped_column(Integer)  # 出差津贴
    comprehensive_subsidy: Mapped[int] = mapped_column(Integer)  # 综合补贴
    other_subsidy: Mapped[int] = mapped_column(Integer)  # 其他津贴
    performance_rating: Mapped[str] = mapped_column(String(50))  # 评比绩效
    retroactive_payment: Mapped[int] = mapped_column(Integer)  # 补付前期
    payment_difference: Mapped[int] = mapped_column(Integer)  # 补付差额
    absence_deduction: Mapped[int] = mapped_column(Integer)  # 缺勤扣款
    other_deduction: Mapped[int] = mapped_column(Integer)  # 其他扣款
    payable_salary: Mapped[int] = mapped_column(Integer)  # 应付工资
    tax_deduction_only: Mapped[int] = mapped_column(Integer)  # 仅扣税
    urban_pension_personal: Mapped[int] = mapped_column(Integer)  # 城保养老保险个人
    urban_medical_insurance_personal: Mapped[int] = mapped_column(Integer)  # 城保医疗保险个人
    urban_unemployment_insurance_personal: Mapped[int] = mapped_column(Integer)  # 城保失业保险个人
    provident_fund: Mapped[int] = mapped_column(Integer)  # 公积金
    social_insurance_total: Mapped[int] = mapped_column(Integer)  # 五险一金小计
    pre_tax_salary: Mapped[int] = mapped_column(Integer)  # 税前工资
    total_children_education_deduction: Mapped[int] = mapped_column(Integer)  # 累计子女教育支出扣除
    total_elderly_support_deduction: Mapped[int] = mapped_column(Integer)  # 累计赡养老人支出扣除
    total_continuing_education_deduction: Mapped[int] = mapped_column(Integer)  # 累计继续教育支出扣除
    total_mortgage_interest_deduction: Mapped[int] = mapped_column(Integer)  # 累计住房贷款利息支出扣除
    total_rent_deduction: Mapped[int] = mapped_column(Integer)  # 累计住房租金支出扣除
    total_childcare_expense_deduction: Mapped[int] = mapped_column(Integer)  # 累计婴幼儿照护费用扣除
    personal_income_tax: Mapped[int] = mapped_column(Integer)  # 个人所得税
    tax_adjustment: Mapped[int] = mapped_column(Integer)  # 个税补/扣
    total_deduction: Mapped[int] = mapped_column(Integer)  # 扣款小计
    net_salary: Mapped[int] = mapped_column(Integer)  # 实得工资
    one_time_bonus: Mapped[int] = mapped_column(Integer)  # 一次性奖金
    bonus_tax: Mapped[int] = mapped_column(Integer)  # 奖金税
    net_amount: Mapped[int] = mapped_column(Integer)  # 实得金额


    