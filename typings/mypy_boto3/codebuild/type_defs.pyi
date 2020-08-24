from mypy_boto3_codebuild.type_defs import (
    BatchRestrictionsTypeDef,
    BuildArtifactsTypeDef,
    BuildBatchPhaseTypeDef,
    BuildBatchTypeDef,
    BuildGroupTypeDef,
    BuildNotDeletedTypeDef,
    BuildPhaseTypeDef,
    BuildStatusConfigTypeDef,
    BuildSummaryTypeDef,
    BuildTypeDef,
    CloudWatchLogsConfigTypeDef,
    CodeCoverageReportSummaryTypeDef,
    CodeCoverageTypeDef,
    DebugSessionTypeDef,
    EnvironmentImageTypeDef,
    EnvironmentLanguageTypeDef,
    EnvironmentPlatformTypeDef,
    EnvironmentVariableTypeDef,
    ExportedEnvironmentVariableTypeDef,
    GitSubmodulesConfigTypeDef,
    LogsConfigTypeDef,
    LogsLocationTypeDef,
    NetworkInterfaceTypeDef,
    PhaseContextTypeDef,
    ProjectArtifactsTypeDef,
    ProjectBadgeTypeDef,
    ProjectBuildBatchConfigTypeDef,
    ProjectCacheTypeDef,
    ProjectEnvironmentTypeDef,
    ProjectFileSystemLocationTypeDef,
    ProjectSourceTypeDef,
    ProjectSourceVersionTypeDef,
    ProjectTypeDef,
    RegistryCredentialTypeDef,
    ReportExportConfigTypeDef,
    ReportGroupTypeDef,
    ReportTypeDef,
    ResolvedArtifactTypeDef,
    S3LogsConfigTypeDef,
    S3ReportExportConfigTypeDef,
    SourceAuthTypeDef,
    SourceCredentialsInfoTypeDef,
    TagTypeDef,
    TestCaseTypeDef,
    TestReportSummaryTypeDef,
    VpcConfigTypeDef,
    WebhookFilterTypeDef,
    WebhookTypeDef,
    BatchDeleteBuildsOutputTypeDef,
    BatchGetBuildBatchesOutputTypeDef,
    BatchGetBuildsOutputTypeDef,
    BatchGetProjectsOutputTypeDef,
    BatchGetReportGroupsOutputTypeDef,
    BatchGetReportsOutputTypeDef,
    BuildBatchFilterTypeDef,
    CreateProjectOutputTypeDef,
    CreateReportGroupOutputTypeDef,
    CreateWebhookOutputTypeDef,
    DeleteBuildBatchOutputTypeDef,
    DeleteSourceCredentialsOutputTypeDef,
    DescribeCodeCoveragesOutputTypeDef,
    DescribeTestCasesOutputTypeDef,
    GetResourcePolicyOutputTypeDef,
    ImportSourceCredentialsOutputTypeDef,
    ListBuildBatchesForProjectOutputTypeDef,
    ListBuildBatchesOutputTypeDef,
    ListBuildsForProjectOutputTypeDef,
    ListBuildsOutputTypeDef,
    ListCuratedEnvironmentImagesOutputTypeDef,
    ListProjectsOutputTypeDef,
    ListReportGroupsOutputTypeDef,
    ListReportsForReportGroupOutputTypeDef,
    ListReportsOutputTypeDef,
    ListSharedProjectsOutputTypeDef,
    ListSharedReportGroupsOutputTypeDef,
    ListSourceCredentialsOutputTypeDef,
    PaginatorConfigTypeDef,
    PutResourcePolicyOutputTypeDef,
    ReportFilterTypeDef,
    RetryBuildBatchOutputTypeDef,
    RetryBuildOutputTypeDef,
    StartBuildBatchOutputTypeDef,
    StartBuildOutputTypeDef,
    StopBuildBatchOutputTypeDef,
    StopBuildOutputTypeDef,
    TestCaseFilterTypeDef,
    UpdateProjectOutputTypeDef,
    UpdateReportGroupOutputTypeDef,
    UpdateWebhookOutputTypeDef,
)

__all__ = (
    "BatchRestrictionsTypeDef",
    "BuildArtifactsTypeDef",
    "BuildBatchPhaseTypeDef",
    "BuildBatchTypeDef",
    "BuildGroupTypeDef",
    "BuildNotDeletedTypeDef",
    "BuildPhaseTypeDef",
    "BuildStatusConfigTypeDef",
    "BuildSummaryTypeDef",
    "BuildTypeDef",
    "CloudWatchLogsConfigTypeDef",
    "CodeCoverageReportSummaryTypeDef",
    "CodeCoverageTypeDef",
    "DebugSessionTypeDef",
    "EnvironmentImageTypeDef",
    "EnvironmentLanguageTypeDef",
    "EnvironmentPlatformTypeDef",
    "EnvironmentVariableTypeDef",
    "ExportedEnvironmentVariableTypeDef",
    "GitSubmodulesConfigTypeDef",
    "LogsConfigTypeDef",
    "LogsLocationTypeDef",
    "NetworkInterfaceTypeDef",
    "PhaseContextTypeDef",
    "ProjectArtifactsTypeDef",
    "ProjectBadgeTypeDef",
    "ProjectBuildBatchConfigTypeDef",
    "ProjectCacheTypeDef",
    "ProjectEnvironmentTypeDef",
    "ProjectFileSystemLocationTypeDef",
    "ProjectSourceTypeDef",
    "ProjectSourceVersionTypeDef",
    "ProjectTypeDef",
    "RegistryCredentialTypeDef",
    "ReportExportConfigTypeDef",
    "ReportGroupTypeDef",
    "ReportTypeDef",
    "ResolvedArtifactTypeDef",
    "S3LogsConfigTypeDef",
    "S3ReportExportConfigTypeDef",
    "SourceAuthTypeDef",
    "SourceCredentialsInfoTypeDef",
    "TagTypeDef",
    "TestCaseTypeDef",
    "TestReportSummaryTypeDef",
    "VpcConfigTypeDef",
    "WebhookFilterTypeDef",
    "WebhookTypeDef",
    "BatchDeleteBuildsOutputTypeDef",
    "BatchGetBuildBatchesOutputTypeDef",
    "BatchGetBuildsOutputTypeDef",
    "BatchGetProjectsOutputTypeDef",
    "BatchGetReportGroupsOutputTypeDef",
    "BatchGetReportsOutputTypeDef",
    "BuildBatchFilterTypeDef",
    "CreateProjectOutputTypeDef",
    "CreateReportGroupOutputTypeDef",
    "CreateWebhookOutputTypeDef",
    "DeleteBuildBatchOutputTypeDef",
    "DeleteSourceCredentialsOutputTypeDef",
    "DescribeCodeCoveragesOutputTypeDef",
    "DescribeTestCasesOutputTypeDef",
    "GetResourcePolicyOutputTypeDef",
    "ImportSourceCredentialsOutputTypeDef",
    "ListBuildBatchesForProjectOutputTypeDef",
    "ListBuildBatchesOutputTypeDef",
    "ListBuildsForProjectOutputTypeDef",
    "ListBuildsOutputTypeDef",
    "ListCuratedEnvironmentImagesOutputTypeDef",
    "ListProjectsOutputTypeDef",
    "ListReportGroupsOutputTypeDef",
    "ListReportsForReportGroupOutputTypeDef",
    "ListReportsOutputTypeDef",
    "ListSharedProjectsOutputTypeDef",
    "ListSharedReportGroupsOutputTypeDef",
    "ListSourceCredentialsOutputTypeDef",
    "PaginatorConfigTypeDef",
    "PutResourcePolicyOutputTypeDef",
    "ReportFilterTypeDef",
    "RetryBuildBatchOutputTypeDef",
    "RetryBuildOutputTypeDef",
    "StartBuildBatchOutputTypeDef",
    "StartBuildOutputTypeDef",
    "StopBuildBatchOutputTypeDef",
    "StopBuildOutputTypeDef",
    "TestCaseFilterTypeDef",
    "UpdateProjectOutputTypeDef",
    "UpdateReportGroupOutputTypeDef",
    "UpdateWebhookOutputTypeDef",
)