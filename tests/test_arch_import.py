import pytest
from wom.app_logic.copy_archive_case import arch_import
from tests.fixtures.arch_load import d_arch, d_adm_copy, d_dynamic_copy


@pytest.mark.parametrize("d_result, d_archive, regimen", [
    (d_arch, d_arch, 'full'),
    (d_adm_copy, d_arch, 'only_adm'),
    (d_dynamic_copy, d_arch, 'dynamic')])
def test_arch_import(d_result, d_archive, regimen):
    assert d_result == arch_import({}, d_archive, regimen,
                                   add_base=False)
