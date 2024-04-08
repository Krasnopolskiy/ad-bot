from aiogram.types import BufferedInputFile, InputMediaDocument
from boto3 import Session
from botocore.client import BaseClient
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class S3Config(BaseSettings):
    model_config = SettingsConfigDict(extra="allow")

    host: str = Field(alias="MINIO_HOST")
    region: str = Field(alias="MINIO_REGION")
    bucket_name: str = Field(alias="MINIO_BUCKET_NAME")
    root_user: str = Field(alias="MINIO_ROOT_USER")
    root_password: str = Field(alias="MINIO_ROOT_PASSWORD")

    @property
    def client(self) -> BaseClient:
        return Session(region_name=self.region,).client(
            service_name="s3",
            endpoint_url=f"http://{self.host}:9000/",
            aws_access_key_id=self.root_user,
            aws_secret_access_key=self.root_password,
        )

    def read_item(self, path: str) -> bytes:
        obj = self.client.get_object(Bucket=self.bucket_name, Key=path)
        return obj["Body"].read()

    def read_document(self, path: str) -> InputMediaDocument:
        item = self.read_item(path)
        return InputMediaDocument(media=BufferedInputFile(item, path))
