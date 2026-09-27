"""Boundary tests for THROTTLE."""
CONTRACT="contracts/throttle.py";SDK="v0.2.12"
def test_seal_needs_class(direct_vm,direct_deploy,direct_alice):
 direct_vm.sender=direct_alice;c=direct_deploy(CONTRACT,sdk_version=SDK);p=c.create_policy("x")
 with direct_vm.expect_revert("at least one class"):c.seal_policy(p)
def test_invalid_capacity(direct_vm,direct_deploy,direct_alice):
 direct_vm.sender=direct_alice;c=direct_deploy(CONTRACT,sdk_version=SDK);p=c.create_policy("x")
 with direct_vm.expect_revert("invalid capacity"):c.add_class(p,"x","effect",0)
def test_requires_sealed(direct_vm,direct_deploy,direct_alice):
 direct_vm.sender=direct_alice;c=direct_deploy(CONTRACT,sdk_version=SDK);p=c.create_policy("x");c.add_class(p,"x","effect",10)
 with direct_vm.expect_revert("must be sealed"):c.authorize_operation(p,"x",1)
def test_invalid_units(direct_vm,direct_deploy,direct_alice):
 direct_vm.sender=direct_alice;c=direct_deploy(CONTRACT,sdk_version=SDK);p=c.create_policy("x");c.add_class(p,"x","effect",10);c.seal_policy(p)
 with direct_vm.expect_revert("invalid requested_units"):c.authorize_operation(p,"x",0)
def test_constants(direct_vm,direct_deploy):
 c=direct_deploy(CONTRACT,sdk_version=SDK);x=c.protocol_constants();assert x["decision_allowed"]==1 and x["decision_exhausted"]==2 and x["decision_ambiguous"]==3 and x["max_classes"]==8
def test_runtime_chain(direct_vm,direct_deploy):
 c=direct_deploy(CONTRACT,sdk_version=SDK);assert int(c.runtime_chain_id())>=0
