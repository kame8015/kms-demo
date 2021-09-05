import app.app as app
import boto3
import pytest
from moto import mock_kms

AWS_REGION = "ap-northeast-1"


@pytest.fixture(scope="module", autouse=True)
def setup_kms():
    mocker_kms = mock_kms()
    mocker_kms.start()

    # appのkmsをmock
    app.kms = boto3.client(service_name="kms", region_name=AWS_REGION)

    yield app.kms

    mocker_kms.stop()


def test_ok_encrypt_decrypt_text(setup_kms):
    """
    正常系: 暗号化・復号化する.
    期待値: 適切に処理され、もとのプレーンテキストと一致する.
    """
    # given
    kms = setup_kms
    app.key_id = kms.create_key()["KeyMetadata"]["KeyId"]

    plain_text = "sample_data"

    # when
    ## 暗号化
    ret_encrypt = app.encrypt_plain_text(plain_text)
    ## 復号化
    ret_decrypt = app.decrypt_plain_text(ret_encrypt)

    # then
    assert ret_decrypt == plain_text
