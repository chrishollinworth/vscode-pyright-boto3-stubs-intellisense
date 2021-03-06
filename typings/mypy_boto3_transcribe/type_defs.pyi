"""
Main interface for transcribe service type definitions.

Usage::

    ```python
    from mypy_boto3_transcribe.type_defs import ContentRedactionTypeDef

    data: ContentRedactionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ContentRedactionTypeDef",
    "InputDataConfigTypeDef",
    "JobExecutionSettingsTypeDef",
    "LanguageModelTypeDef",
    "MediaTypeDef",
    "MedicalTranscriptTypeDef",
    "MedicalTranscriptionJobSummaryTypeDef",
    "MedicalTranscriptionJobTypeDef",
    "MedicalTranscriptionSettingTypeDef",
    "ModelSettingsTypeDef",
    "SettingsTypeDef",
    "TranscriptTypeDef",
    "TranscriptionJobSummaryTypeDef",
    "TranscriptionJobTypeDef",
    "VocabularyFilterInfoTypeDef",
    "VocabularyInfoTypeDef",
    "CreateLanguageModelResponseTypeDef",
    "CreateMedicalVocabularyResponseTypeDef",
    "CreateVocabularyFilterResponseTypeDef",
    "CreateVocabularyResponseTypeDef",
    "DescribeLanguageModelResponseTypeDef",
    "GetMedicalTranscriptionJobResponseTypeDef",
    "GetMedicalVocabularyResponseTypeDef",
    "GetTranscriptionJobResponseTypeDef",
    "GetVocabularyFilterResponseTypeDef",
    "GetVocabularyResponseTypeDef",
    "ListLanguageModelsResponseTypeDef",
    "ListMedicalTranscriptionJobsResponseTypeDef",
    "ListMedicalVocabulariesResponseTypeDef",
    "ListTranscriptionJobsResponseTypeDef",
    "ListVocabulariesResponseTypeDef",
    "ListVocabularyFiltersResponseTypeDef",
    "StartMedicalTranscriptionJobResponseTypeDef",
    "StartTranscriptionJobResponseTypeDef",
    "UpdateMedicalVocabularyResponseTypeDef",
    "UpdateVocabularyFilterResponseTypeDef",
    "UpdateVocabularyResponseTypeDef",
)

ContentRedactionTypeDef = TypedDict(
    "ContentRedactionTypeDef",
    {
        "RedactionType": Literal["PII"],
        "RedactionOutput": Literal["redacted", "redacted_and_unredacted"],
    },
)

_RequiredInputDataConfigTypeDef = TypedDict(
    "_RequiredInputDataConfigTypeDef", {"S3Uri": str, "DataAccessRoleArn": str}
)
_OptionalInputDataConfigTypeDef = TypedDict(
    "_OptionalInputDataConfigTypeDef", {"TuningDataS3Uri": str}, total=False
)


class InputDataConfigTypeDef(_RequiredInputDataConfigTypeDef, _OptionalInputDataConfigTypeDef):
    pass


JobExecutionSettingsTypeDef = TypedDict(
    "JobExecutionSettingsTypeDef",
    {"AllowDeferredExecution": bool, "DataAccessRoleArn": str},
    total=False,
)

LanguageModelTypeDef = TypedDict(
    "LanguageModelTypeDef",
    {
        "ModelName": str,
        "CreateTime": datetime,
        "LastModifiedTime": datetime,
        "LanguageCode": Literal["en-US"],
        "BaseModelName": Literal["NarrowBand", "WideBand"],
        "ModelStatus": Literal["IN_PROGRESS", "FAILED", "COMPLETED"],
        "UpgradeAvailability": bool,
        "FailureReason": str,
        "InputDataConfig": "InputDataConfigTypeDef",
    },
    total=False,
)

MediaTypeDef = TypedDict("MediaTypeDef", {"MediaFileUri": str}, total=False)

MedicalTranscriptTypeDef = TypedDict(
    "MedicalTranscriptTypeDef", {"TranscriptFileUri": str}, total=False
)

MedicalTranscriptionJobSummaryTypeDef = TypedDict(
    "MedicalTranscriptionJobSummaryTypeDef",
    {
        "MedicalTranscriptionJobName": str,
        "CreationTime": datetime,
        "StartTime": datetime,
        "CompletionTime": datetime,
        "LanguageCode": Literal[
            "af-ZA",
            "ar-AE",
            "ar-SA",
            "cy-GB",
            "da-DK",
            "de-CH",
            "de-DE",
            "en-AB",
            "en-AU",
            "en-GB",
            "en-IE",
            "en-IN",
            "en-US",
            "en-WL",
            "es-ES",
            "es-US",
            "fa-IR",
            "fr-CA",
            "fr-FR",
            "ga-IE",
            "gd-GB",
            "he-IL",
            "hi-IN",
            "id-ID",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "ms-MY",
            "nl-NL",
            "pt-BR",
            "pt-PT",
            "ru-RU",
            "ta-IN",
            "te-IN",
            "tr-TR",
            "zh-CN",
        ],
        "TranscriptionJobStatus": Literal["QUEUED", "IN_PROGRESS", "FAILED", "COMPLETED"],
        "FailureReason": str,
        "OutputLocationType": Literal["CUSTOMER_BUCKET", "SERVICE_BUCKET"],
        "Specialty": Literal["PRIMARYCARE"],
        "Type": Literal["CONVERSATION", "DICTATION"],
    },
    total=False,
)

MedicalTranscriptionJobTypeDef = TypedDict(
    "MedicalTranscriptionJobTypeDef",
    {
        "MedicalTranscriptionJobName": str,
        "TranscriptionJobStatus": Literal["QUEUED", "IN_PROGRESS", "FAILED", "COMPLETED"],
        "LanguageCode": Literal[
            "af-ZA",
            "ar-AE",
            "ar-SA",
            "cy-GB",
            "da-DK",
            "de-CH",
            "de-DE",
            "en-AB",
            "en-AU",
            "en-GB",
            "en-IE",
            "en-IN",
            "en-US",
            "en-WL",
            "es-ES",
            "es-US",
            "fa-IR",
            "fr-CA",
            "fr-FR",
            "ga-IE",
            "gd-GB",
            "he-IL",
            "hi-IN",
            "id-ID",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "ms-MY",
            "nl-NL",
            "pt-BR",
            "pt-PT",
            "ru-RU",
            "ta-IN",
            "te-IN",
            "tr-TR",
            "zh-CN",
        ],
        "MediaSampleRateHertz": int,
        "MediaFormat": Literal["mp3", "mp4", "wav", "flac", "ogg", "amr", "webm"],
        "Media": "MediaTypeDef",
        "Transcript": "MedicalTranscriptTypeDef",
        "StartTime": datetime,
        "CreationTime": datetime,
        "CompletionTime": datetime,
        "FailureReason": str,
        "Settings": "MedicalTranscriptionSettingTypeDef",
        "Specialty": Literal["PRIMARYCARE"],
        "Type": Literal["CONVERSATION", "DICTATION"],
    },
    total=False,
)

MedicalTranscriptionSettingTypeDef = TypedDict(
    "MedicalTranscriptionSettingTypeDef",
    {
        "ShowSpeakerLabels": bool,
        "MaxSpeakerLabels": int,
        "ChannelIdentification": bool,
        "ShowAlternatives": bool,
        "MaxAlternatives": int,
        "VocabularyName": str,
    },
    total=False,
)

ModelSettingsTypeDef = TypedDict("ModelSettingsTypeDef", {"LanguageModelName": str}, total=False)

SettingsTypeDef = TypedDict(
    "SettingsTypeDef",
    {
        "VocabularyName": str,
        "ShowSpeakerLabels": bool,
        "MaxSpeakerLabels": int,
        "ChannelIdentification": bool,
        "ShowAlternatives": bool,
        "MaxAlternatives": int,
        "VocabularyFilterName": str,
        "VocabularyFilterMethod": Literal["remove", "mask"],
    },
    total=False,
)

TranscriptTypeDef = TypedDict(
    "TranscriptTypeDef", {"TranscriptFileUri": str, "RedactedTranscriptFileUri": str}, total=False
)

TranscriptionJobSummaryTypeDef = TypedDict(
    "TranscriptionJobSummaryTypeDef",
    {
        "TranscriptionJobName": str,
        "CreationTime": datetime,
        "StartTime": datetime,
        "CompletionTime": datetime,
        "LanguageCode": Literal[
            "af-ZA",
            "ar-AE",
            "ar-SA",
            "cy-GB",
            "da-DK",
            "de-CH",
            "de-DE",
            "en-AB",
            "en-AU",
            "en-GB",
            "en-IE",
            "en-IN",
            "en-US",
            "en-WL",
            "es-ES",
            "es-US",
            "fa-IR",
            "fr-CA",
            "fr-FR",
            "ga-IE",
            "gd-GB",
            "he-IL",
            "hi-IN",
            "id-ID",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "ms-MY",
            "nl-NL",
            "pt-BR",
            "pt-PT",
            "ru-RU",
            "ta-IN",
            "te-IN",
            "tr-TR",
            "zh-CN",
        ],
        "TranscriptionJobStatus": Literal["QUEUED", "IN_PROGRESS", "FAILED", "COMPLETED"],
        "FailureReason": str,
        "OutputLocationType": Literal["CUSTOMER_BUCKET", "SERVICE_BUCKET"],
        "ContentRedaction": "ContentRedactionTypeDef",
        "ModelSettings": "ModelSettingsTypeDef",
        "IdentifyLanguage": bool,
        "IdentifiedLanguageScore": float,
    },
    total=False,
)

TranscriptionJobTypeDef = TypedDict(
    "TranscriptionJobTypeDef",
    {
        "TranscriptionJobName": str,
        "TranscriptionJobStatus": Literal["QUEUED", "IN_PROGRESS", "FAILED", "COMPLETED"],
        "LanguageCode": Literal[
            "af-ZA",
            "ar-AE",
            "ar-SA",
            "cy-GB",
            "da-DK",
            "de-CH",
            "de-DE",
            "en-AB",
            "en-AU",
            "en-GB",
            "en-IE",
            "en-IN",
            "en-US",
            "en-WL",
            "es-ES",
            "es-US",
            "fa-IR",
            "fr-CA",
            "fr-FR",
            "ga-IE",
            "gd-GB",
            "he-IL",
            "hi-IN",
            "id-ID",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "ms-MY",
            "nl-NL",
            "pt-BR",
            "pt-PT",
            "ru-RU",
            "ta-IN",
            "te-IN",
            "tr-TR",
            "zh-CN",
        ],
        "MediaSampleRateHertz": int,
        "MediaFormat": Literal["mp3", "mp4", "wav", "flac", "ogg", "amr", "webm"],
        "Media": "MediaTypeDef",
        "Transcript": "TranscriptTypeDef",
        "StartTime": datetime,
        "CreationTime": datetime,
        "CompletionTime": datetime,
        "FailureReason": str,
        "Settings": "SettingsTypeDef",
        "ModelSettings": "ModelSettingsTypeDef",
        "JobExecutionSettings": "JobExecutionSettingsTypeDef",
        "ContentRedaction": "ContentRedactionTypeDef",
        "IdentifyLanguage": bool,
        "LanguageOptions": List[
            Literal[
                "af-ZA",
                "ar-AE",
                "ar-SA",
                "cy-GB",
                "da-DK",
                "de-CH",
                "de-DE",
                "en-AB",
                "en-AU",
                "en-GB",
                "en-IE",
                "en-IN",
                "en-US",
                "en-WL",
                "es-ES",
                "es-US",
                "fa-IR",
                "fr-CA",
                "fr-FR",
                "ga-IE",
                "gd-GB",
                "he-IL",
                "hi-IN",
                "id-ID",
                "it-IT",
                "ja-JP",
                "ko-KR",
                "ms-MY",
                "nl-NL",
                "pt-BR",
                "pt-PT",
                "ru-RU",
                "ta-IN",
                "te-IN",
                "tr-TR",
                "zh-CN",
            ]
        ],
        "IdentifiedLanguageScore": float,
    },
    total=False,
)

VocabularyFilterInfoTypeDef = TypedDict(
    "VocabularyFilterInfoTypeDef",
    {
        "VocabularyFilterName": str,
        "LanguageCode": Literal[
            "af-ZA",
            "ar-AE",
            "ar-SA",
            "cy-GB",
            "da-DK",
            "de-CH",
            "de-DE",
            "en-AB",
            "en-AU",
            "en-GB",
            "en-IE",
            "en-IN",
            "en-US",
            "en-WL",
            "es-ES",
            "es-US",
            "fa-IR",
            "fr-CA",
            "fr-FR",
            "ga-IE",
            "gd-GB",
            "he-IL",
            "hi-IN",
            "id-ID",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "ms-MY",
            "nl-NL",
            "pt-BR",
            "pt-PT",
            "ru-RU",
            "ta-IN",
            "te-IN",
            "tr-TR",
            "zh-CN",
        ],
        "LastModifiedTime": datetime,
    },
    total=False,
)

VocabularyInfoTypeDef = TypedDict(
    "VocabularyInfoTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": Literal[
            "af-ZA",
            "ar-AE",
            "ar-SA",
            "cy-GB",
            "da-DK",
            "de-CH",
            "de-DE",
            "en-AB",
            "en-AU",
            "en-GB",
            "en-IE",
            "en-IN",
            "en-US",
            "en-WL",
            "es-ES",
            "es-US",
            "fa-IR",
            "fr-CA",
            "fr-FR",
            "ga-IE",
            "gd-GB",
            "he-IL",
            "hi-IN",
            "id-ID",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "ms-MY",
            "nl-NL",
            "pt-BR",
            "pt-PT",
            "ru-RU",
            "ta-IN",
            "te-IN",
            "tr-TR",
            "zh-CN",
        ],
        "LastModifiedTime": datetime,
        "VocabularyState": Literal["PENDING", "READY", "FAILED"],
    },
    total=False,
)

CreateLanguageModelResponseTypeDef = TypedDict(
    "CreateLanguageModelResponseTypeDef",
    {
        "LanguageCode": Literal["en-US"],
        "BaseModelName": Literal["NarrowBand", "WideBand"],
        "ModelName": str,
        "InputDataConfig": "InputDataConfigTypeDef",
        "ModelStatus": Literal["IN_PROGRESS", "FAILED", "COMPLETED"],
    },
    total=False,
)

CreateMedicalVocabularyResponseTypeDef = TypedDict(
    "CreateMedicalVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": Literal[
            "af-ZA",
            "ar-AE",
            "ar-SA",
            "cy-GB",
            "da-DK",
            "de-CH",
            "de-DE",
            "en-AB",
            "en-AU",
            "en-GB",
            "en-IE",
            "en-IN",
            "en-US",
            "en-WL",
            "es-ES",
            "es-US",
            "fa-IR",
            "fr-CA",
            "fr-FR",
            "ga-IE",
            "gd-GB",
            "he-IL",
            "hi-IN",
            "id-ID",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "ms-MY",
            "nl-NL",
            "pt-BR",
            "pt-PT",
            "ru-RU",
            "ta-IN",
            "te-IN",
            "tr-TR",
            "zh-CN",
        ],
        "VocabularyState": Literal["PENDING", "READY", "FAILED"],
        "LastModifiedTime": datetime,
        "FailureReason": str,
    },
    total=False,
)

CreateVocabularyFilterResponseTypeDef = TypedDict(
    "CreateVocabularyFilterResponseTypeDef",
    {
        "VocabularyFilterName": str,
        "LanguageCode": Literal[
            "af-ZA",
            "ar-AE",
            "ar-SA",
            "cy-GB",
            "da-DK",
            "de-CH",
            "de-DE",
            "en-AB",
            "en-AU",
            "en-GB",
            "en-IE",
            "en-IN",
            "en-US",
            "en-WL",
            "es-ES",
            "es-US",
            "fa-IR",
            "fr-CA",
            "fr-FR",
            "ga-IE",
            "gd-GB",
            "he-IL",
            "hi-IN",
            "id-ID",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "ms-MY",
            "nl-NL",
            "pt-BR",
            "pt-PT",
            "ru-RU",
            "ta-IN",
            "te-IN",
            "tr-TR",
            "zh-CN",
        ],
        "LastModifiedTime": datetime,
    },
    total=False,
)

CreateVocabularyResponseTypeDef = TypedDict(
    "CreateVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": Literal[
            "af-ZA",
            "ar-AE",
            "ar-SA",
            "cy-GB",
            "da-DK",
            "de-CH",
            "de-DE",
            "en-AB",
            "en-AU",
            "en-GB",
            "en-IE",
            "en-IN",
            "en-US",
            "en-WL",
            "es-ES",
            "es-US",
            "fa-IR",
            "fr-CA",
            "fr-FR",
            "ga-IE",
            "gd-GB",
            "he-IL",
            "hi-IN",
            "id-ID",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "ms-MY",
            "nl-NL",
            "pt-BR",
            "pt-PT",
            "ru-RU",
            "ta-IN",
            "te-IN",
            "tr-TR",
            "zh-CN",
        ],
        "VocabularyState": Literal["PENDING", "READY", "FAILED"],
        "LastModifiedTime": datetime,
        "FailureReason": str,
    },
    total=False,
)

DescribeLanguageModelResponseTypeDef = TypedDict(
    "DescribeLanguageModelResponseTypeDef", {"LanguageModel": "LanguageModelTypeDef"}, total=False
)

GetMedicalTranscriptionJobResponseTypeDef = TypedDict(
    "GetMedicalTranscriptionJobResponseTypeDef",
    {"MedicalTranscriptionJob": "MedicalTranscriptionJobTypeDef"},
    total=False,
)

GetMedicalVocabularyResponseTypeDef = TypedDict(
    "GetMedicalVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": Literal[
            "af-ZA",
            "ar-AE",
            "ar-SA",
            "cy-GB",
            "da-DK",
            "de-CH",
            "de-DE",
            "en-AB",
            "en-AU",
            "en-GB",
            "en-IE",
            "en-IN",
            "en-US",
            "en-WL",
            "es-ES",
            "es-US",
            "fa-IR",
            "fr-CA",
            "fr-FR",
            "ga-IE",
            "gd-GB",
            "he-IL",
            "hi-IN",
            "id-ID",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "ms-MY",
            "nl-NL",
            "pt-BR",
            "pt-PT",
            "ru-RU",
            "ta-IN",
            "te-IN",
            "tr-TR",
            "zh-CN",
        ],
        "VocabularyState": Literal["PENDING", "READY", "FAILED"],
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "DownloadUri": str,
    },
    total=False,
)

GetTranscriptionJobResponseTypeDef = TypedDict(
    "GetTranscriptionJobResponseTypeDef",
    {"TranscriptionJob": "TranscriptionJobTypeDef"},
    total=False,
)

GetVocabularyFilterResponseTypeDef = TypedDict(
    "GetVocabularyFilterResponseTypeDef",
    {
        "VocabularyFilterName": str,
        "LanguageCode": Literal[
            "af-ZA",
            "ar-AE",
            "ar-SA",
            "cy-GB",
            "da-DK",
            "de-CH",
            "de-DE",
            "en-AB",
            "en-AU",
            "en-GB",
            "en-IE",
            "en-IN",
            "en-US",
            "en-WL",
            "es-ES",
            "es-US",
            "fa-IR",
            "fr-CA",
            "fr-FR",
            "ga-IE",
            "gd-GB",
            "he-IL",
            "hi-IN",
            "id-ID",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "ms-MY",
            "nl-NL",
            "pt-BR",
            "pt-PT",
            "ru-RU",
            "ta-IN",
            "te-IN",
            "tr-TR",
            "zh-CN",
        ],
        "LastModifiedTime": datetime,
        "DownloadUri": str,
    },
    total=False,
)

GetVocabularyResponseTypeDef = TypedDict(
    "GetVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": Literal[
            "af-ZA",
            "ar-AE",
            "ar-SA",
            "cy-GB",
            "da-DK",
            "de-CH",
            "de-DE",
            "en-AB",
            "en-AU",
            "en-GB",
            "en-IE",
            "en-IN",
            "en-US",
            "en-WL",
            "es-ES",
            "es-US",
            "fa-IR",
            "fr-CA",
            "fr-FR",
            "ga-IE",
            "gd-GB",
            "he-IL",
            "hi-IN",
            "id-ID",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "ms-MY",
            "nl-NL",
            "pt-BR",
            "pt-PT",
            "ru-RU",
            "ta-IN",
            "te-IN",
            "tr-TR",
            "zh-CN",
        ],
        "VocabularyState": Literal["PENDING", "READY", "FAILED"],
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "DownloadUri": str,
    },
    total=False,
)

ListLanguageModelsResponseTypeDef = TypedDict(
    "ListLanguageModelsResponseTypeDef",
    {"NextToken": str, "Models": List["LanguageModelTypeDef"]},
    total=False,
)

ListMedicalTranscriptionJobsResponseTypeDef = TypedDict(
    "ListMedicalTranscriptionJobsResponseTypeDef",
    {
        "Status": Literal["QUEUED", "IN_PROGRESS", "FAILED", "COMPLETED"],
        "NextToken": str,
        "MedicalTranscriptionJobSummaries": List["MedicalTranscriptionJobSummaryTypeDef"],
    },
    total=False,
)

ListMedicalVocabulariesResponseTypeDef = TypedDict(
    "ListMedicalVocabulariesResponseTypeDef",
    {
        "Status": Literal["PENDING", "READY", "FAILED"],
        "NextToken": str,
        "Vocabularies": List["VocabularyInfoTypeDef"],
    },
    total=False,
)

ListTranscriptionJobsResponseTypeDef = TypedDict(
    "ListTranscriptionJobsResponseTypeDef",
    {
        "Status": Literal["QUEUED", "IN_PROGRESS", "FAILED", "COMPLETED"],
        "NextToken": str,
        "TranscriptionJobSummaries": List["TranscriptionJobSummaryTypeDef"],
    },
    total=False,
)

ListVocabulariesResponseTypeDef = TypedDict(
    "ListVocabulariesResponseTypeDef",
    {
        "Status": Literal["PENDING", "READY", "FAILED"],
        "NextToken": str,
        "Vocabularies": List["VocabularyInfoTypeDef"],
    },
    total=False,
)

ListVocabularyFiltersResponseTypeDef = TypedDict(
    "ListVocabularyFiltersResponseTypeDef",
    {"NextToken": str, "VocabularyFilters": List["VocabularyFilterInfoTypeDef"]},
    total=False,
)

StartMedicalTranscriptionJobResponseTypeDef = TypedDict(
    "StartMedicalTranscriptionJobResponseTypeDef",
    {"MedicalTranscriptionJob": "MedicalTranscriptionJobTypeDef"},
    total=False,
)

StartTranscriptionJobResponseTypeDef = TypedDict(
    "StartTranscriptionJobResponseTypeDef",
    {"TranscriptionJob": "TranscriptionJobTypeDef"},
    total=False,
)

UpdateMedicalVocabularyResponseTypeDef = TypedDict(
    "UpdateMedicalVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": Literal[
            "af-ZA",
            "ar-AE",
            "ar-SA",
            "cy-GB",
            "da-DK",
            "de-CH",
            "de-DE",
            "en-AB",
            "en-AU",
            "en-GB",
            "en-IE",
            "en-IN",
            "en-US",
            "en-WL",
            "es-ES",
            "es-US",
            "fa-IR",
            "fr-CA",
            "fr-FR",
            "ga-IE",
            "gd-GB",
            "he-IL",
            "hi-IN",
            "id-ID",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "ms-MY",
            "nl-NL",
            "pt-BR",
            "pt-PT",
            "ru-RU",
            "ta-IN",
            "te-IN",
            "tr-TR",
            "zh-CN",
        ],
        "LastModifiedTime": datetime,
        "VocabularyState": Literal["PENDING", "READY", "FAILED"],
    },
    total=False,
)

UpdateVocabularyFilterResponseTypeDef = TypedDict(
    "UpdateVocabularyFilterResponseTypeDef",
    {
        "VocabularyFilterName": str,
        "LanguageCode": Literal[
            "af-ZA",
            "ar-AE",
            "ar-SA",
            "cy-GB",
            "da-DK",
            "de-CH",
            "de-DE",
            "en-AB",
            "en-AU",
            "en-GB",
            "en-IE",
            "en-IN",
            "en-US",
            "en-WL",
            "es-ES",
            "es-US",
            "fa-IR",
            "fr-CA",
            "fr-FR",
            "ga-IE",
            "gd-GB",
            "he-IL",
            "hi-IN",
            "id-ID",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "ms-MY",
            "nl-NL",
            "pt-BR",
            "pt-PT",
            "ru-RU",
            "ta-IN",
            "te-IN",
            "tr-TR",
            "zh-CN",
        ],
        "LastModifiedTime": datetime,
    },
    total=False,
)

UpdateVocabularyResponseTypeDef = TypedDict(
    "UpdateVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": Literal[
            "af-ZA",
            "ar-AE",
            "ar-SA",
            "cy-GB",
            "da-DK",
            "de-CH",
            "de-DE",
            "en-AB",
            "en-AU",
            "en-GB",
            "en-IE",
            "en-IN",
            "en-US",
            "en-WL",
            "es-ES",
            "es-US",
            "fa-IR",
            "fr-CA",
            "fr-FR",
            "ga-IE",
            "gd-GB",
            "he-IL",
            "hi-IN",
            "id-ID",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "ms-MY",
            "nl-NL",
            "pt-BR",
            "pt-PT",
            "ru-RU",
            "ta-IN",
            "te-IN",
            "tr-TR",
            "zh-CN",
        ],
        "LastModifiedTime": datetime,
        "VocabularyState": Literal["PENDING", "READY", "FAILED"],
    },
    total=False,
)
