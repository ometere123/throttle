"""Live stable-Studionet lifecycle for THROTTLE."""
from gltest import get_contract_factory,get_default_account
from gltest.assertions import tx_execution_succeeded
TX={"consensus_max_rotations":3,"wait_interval":10000,"wait_retries":30}
def ok(r):assert tx_execution_succeeded(r),r
def test_live_semantic_budget_lifecycle():
 a=get_default_account();c=get_contract_factory(contract_file_path="throttle.py").deploy(account=a,**TX);assert c.address
 ok(c.create_policy(args=["Autonomous agent effect budgets"]).transact(**TX))
 ok(c.add_class(args=[1,"Vendor payment","Operations whose material effect is sending or committing value to an external vendor.",100]).transact(**TX))
 ok(c.add_class(args=[1,"Customer data export","Operations whose material effect is disclosing or exporting customer personal data to an external recipient.",50]).transact(**TX))
 ok(c.seal_policy(args=[1]).transact(**TX))
 ok(c.authorize_operation(args=[1,"Send 60 units to supplier Acme for invoice 7.",60]).transact(**TX))
 d1=c.get_decision(args=[1]).call();assert d1["status"]==1 and d1["class_id"]==1 and d1["remaining_after"]==40
 ok(c.authorize_operation(args=[1,"Settle Acme invoice 8 by remitting 30 units to the vendor.",30]).transact(**TX))
 d2=c.get_decision(args=[2]).call();assert d2["status"]==1 and d2["class_id"]==1 and d2["remaining_after"]==10
 ok(c.authorize_operation(args=[1,"Pay supplier Acme another 20 units for invoice 9.",20]).transact(**TX))
 d3=c.get_decision(args=[3]).call();assert d3["status"]==2 and c.remaining(args=[1]).call()==10
 ok(c.authorize_operation(args=[1,"Export the customer's personal profile to external analytics partner DataCo.",10]).transact(**TX))
 d4=c.get_decision(args=[4]).call();assert d4["status"]==1 and d4["class_id"]==2 and d4["remaining_after"]==40
