from mypy_boto3_codecommit.type_defs import (
    ApprovalRuleEventMetadataTypeDef,
    ApprovalRuleOverriddenEventMetadataTypeDef,
    ApprovalRuleTemplateTypeDef,
    ApprovalRuleTypeDef,
    ApprovalStateChangedEventMetadataTypeDef,
    ApprovalTypeDef,
    BatchAssociateApprovalRuleTemplateWithRepositoriesErrorTypeDef,
    BatchDescribeMergeConflictsErrorTypeDef,
    BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorTypeDef,
    BatchGetCommitsErrorTypeDef,
    BlobMetadataTypeDef,
    BranchInfoTypeDef,
    CommentTypeDef,
    CommentsForComparedCommitTypeDef,
    CommentsForPullRequestTypeDef,
    CommitTypeDef,
    ConflictMetadataTypeDef,
    ConflictTypeDef,
    DeleteFileEntryTypeDef,
    DifferenceTypeDef,
    EvaluationTypeDef,
    FileMetadataTypeDef,
    FileModesTypeDef,
    FileSizesTypeDef,
    FileTypeDef,
    FolderTypeDef,
    IsBinaryFileTypeDef,
    LocationTypeDef,
    MergeHunkDetailTypeDef,
    MergeHunkTypeDef,
    MergeMetadataTypeDef,
    MergeOperationsTypeDef,
    ObjectTypesTypeDef,
    OriginApprovalRuleTemplateTypeDef,
    PullRequestCreatedEventMetadataTypeDef,
    PullRequestEventTypeDef,
    PullRequestMergedStateChangedEventMetadataTypeDef,
    PullRequestSourceReferenceUpdatedEventMetadataTypeDef,
    PullRequestStatusChangedEventMetadataTypeDef,
    PullRequestTargetTypeDef,
    PullRequestTypeDef,
    ReactionForCommentTypeDef,
    ReactionValueFormatsTypeDef,
    ReplaceContentEntryTypeDef,
    RepositoryMetadataTypeDef,
    RepositoryNameIdPairTypeDef,
    RepositoryTriggerExecutionFailureTypeDef,
    RepositoryTriggerTypeDef,
    SetFileModeEntryTypeDef,
    SourceFileSpecifierTypeDef,
    SubModuleTypeDef,
    SymbolicLinkTypeDef,
    UserInfoTypeDef,
    BatchAssociateApprovalRuleTemplateWithRepositoriesOutputTypeDef,
    BatchDescribeMergeConflictsOutputTypeDef,
    BatchDisassociateApprovalRuleTemplateFromRepositoriesOutputTypeDef,
    BatchGetCommitsOutputTypeDef,
    BatchGetRepositoriesOutputTypeDef,
    ConflictResolutionTypeDef,
    CreateApprovalRuleTemplateOutputTypeDef,
    CreateCommitOutputTypeDef,
    CreatePullRequestApprovalRuleOutputTypeDef,
    CreatePullRequestOutputTypeDef,
    CreateRepositoryOutputTypeDef,
    CreateUnreferencedMergeCommitOutputTypeDef,
    DeleteApprovalRuleTemplateOutputTypeDef,
    DeleteBranchOutputTypeDef,
    DeleteCommentContentOutputTypeDef,
    DeleteFileOutputTypeDef,
    DeletePullRequestApprovalRuleOutputTypeDef,
    DeleteRepositoryOutputTypeDef,
    DescribeMergeConflictsOutputTypeDef,
    DescribePullRequestEventsOutputTypeDef,
    EvaluatePullRequestApprovalRulesOutputTypeDef,
    GetApprovalRuleTemplateOutputTypeDef,
    GetBlobOutputTypeDef,
    GetBranchOutputTypeDef,
    GetCommentOutputTypeDef,
    GetCommentReactionsOutputTypeDef,
    GetCommentsForComparedCommitOutputTypeDef,
    GetCommentsForPullRequestOutputTypeDef,
    GetCommitOutputTypeDef,
    GetDifferencesOutputTypeDef,
    GetFileOutputTypeDef,
    GetFolderOutputTypeDef,
    GetMergeCommitOutputTypeDef,
    GetMergeConflictsOutputTypeDef,
    GetMergeOptionsOutputTypeDef,
    GetPullRequestApprovalStatesOutputTypeDef,
    GetPullRequestOutputTypeDef,
    GetPullRequestOverrideStateOutputTypeDef,
    GetRepositoryOutputTypeDef,
    GetRepositoryTriggersOutputTypeDef,
    ListApprovalRuleTemplatesOutputTypeDef,
    ListAssociatedApprovalRuleTemplatesForRepositoryOutputTypeDef,
    ListBranchesOutputTypeDef,
    ListPullRequestsOutputTypeDef,
    ListRepositoriesForApprovalRuleTemplateOutputTypeDef,
    ListRepositoriesOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    MergeBranchesByFastForwardOutputTypeDef,
    MergeBranchesBySquashOutputTypeDef,
    MergeBranchesByThreeWayOutputTypeDef,
    MergePullRequestByFastForwardOutputTypeDef,
    MergePullRequestBySquashOutputTypeDef,
    MergePullRequestByThreeWayOutputTypeDef,
    PaginatorConfigTypeDef,
    PostCommentForComparedCommitOutputTypeDef,
    PostCommentForPullRequestOutputTypeDef,
    PostCommentReplyOutputTypeDef,
    PutFileEntryTypeDef,
    PutFileOutputTypeDef,
    PutRepositoryTriggersOutputTypeDef,
    TargetTypeDef,
    TestRepositoryTriggersOutputTypeDef,
    UpdateApprovalRuleTemplateContentOutputTypeDef,
    UpdateApprovalRuleTemplateDescriptionOutputTypeDef,
    UpdateApprovalRuleTemplateNameOutputTypeDef,
    UpdateCommentOutputTypeDef,
    UpdatePullRequestApprovalRuleContentOutputTypeDef,
    UpdatePullRequestDescriptionOutputTypeDef,
    UpdatePullRequestStatusOutputTypeDef,
    UpdatePullRequestTitleOutputTypeDef,
)

__all__ = (
    "ApprovalRuleEventMetadataTypeDef",
    "ApprovalRuleOverriddenEventMetadataTypeDef",
    "ApprovalRuleTemplateTypeDef",
    "ApprovalRuleTypeDef",
    "ApprovalStateChangedEventMetadataTypeDef",
    "ApprovalTypeDef",
    "BatchAssociateApprovalRuleTemplateWithRepositoriesErrorTypeDef",
    "BatchDescribeMergeConflictsErrorTypeDef",
    "BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorTypeDef",
    "BatchGetCommitsErrorTypeDef",
    "BlobMetadataTypeDef",
    "BranchInfoTypeDef",
    "CommentTypeDef",
    "CommentsForComparedCommitTypeDef",
    "CommentsForPullRequestTypeDef",
    "CommitTypeDef",
    "ConflictMetadataTypeDef",
    "ConflictTypeDef",
    "DeleteFileEntryTypeDef",
    "DifferenceTypeDef",
    "EvaluationTypeDef",
    "FileMetadataTypeDef",
    "FileModesTypeDef",
    "FileSizesTypeDef",
    "FileTypeDef",
    "FolderTypeDef",
    "IsBinaryFileTypeDef",
    "LocationTypeDef",
    "MergeHunkDetailTypeDef",
    "MergeHunkTypeDef",
    "MergeMetadataTypeDef",
    "MergeOperationsTypeDef",
    "ObjectTypesTypeDef",
    "OriginApprovalRuleTemplateTypeDef",
    "PullRequestCreatedEventMetadataTypeDef",
    "PullRequestEventTypeDef",
    "PullRequestMergedStateChangedEventMetadataTypeDef",
    "PullRequestSourceReferenceUpdatedEventMetadataTypeDef",
    "PullRequestStatusChangedEventMetadataTypeDef",
    "PullRequestTargetTypeDef",
    "PullRequestTypeDef",
    "ReactionForCommentTypeDef",
    "ReactionValueFormatsTypeDef",
    "ReplaceContentEntryTypeDef",
    "RepositoryMetadataTypeDef",
    "RepositoryNameIdPairTypeDef",
    "RepositoryTriggerExecutionFailureTypeDef",
    "RepositoryTriggerTypeDef",
    "SetFileModeEntryTypeDef",
    "SourceFileSpecifierTypeDef",
    "SubModuleTypeDef",
    "SymbolicLinkTypeDef",
    "UserInfoTypeDef",
    "BatchAssociateApprovalRuleTemplateWithRepositoriesOutputTypeDef",
    "BatchDescribeMergeConflictsOutputTypeDef",
    "BatchDisassociateApprovalRuleTemplateFromRepositoriesOutputTypeDef",
    "BatchGetCommitsOutputTypeDef",
    "BatchGetRepositoriesOutputTypeDef",
    "ConflictResolutionTypeDef",
    "CreateApprovalRuleTemplateOutputTypeDef",
    "CreateCommitOutputTypeDef",
    "CreatePullRequestApprovalRuleOutputTypeDef",
    "CreatePullRequestOutputTypeDef",
    "CreateRepositoryOutputTypeDef",
    "CreateUnreferencedMergeCommitOutputTypeDef",
    "DeleteApprovalRuleTemplateOutputTypeDef",
    "DeleteBranchOutputTypeDef",
    "DeleteCommentContentOutputTypeDef",
    "DeleteFileOutputTypeDef",
    "DeletePullRequestApprovalRuleOutputTypeDef",
    "DeleteRepositoryOutputTypeDef",
    "DescribeMergeConflictsOutputTypeDef",
    "DescribePullRequestEventsOutputTypeDef",
    "EvaluatePullRequestApprovalRulesOutputTypeDef",
    "GetApprovalRuleTemplateOutputTypeDef",
    "GetBlobOutputTypeDef",
    "GetBranchOutputTypeDef",
    "GetCommentOutputTypeDef",
    "GetCommentReactionsOutputTypeDef",
    "GetCommentsForComparedCommitOutputTypeDef",
    "GetCommentsForPullRequestOutputTypeDef",
    "GetCommitOutputTypeDef",
    "GetDifferencesOutputTypeDef",
    "GetFileOutputTypeDef",
    "GetFolderOutputTypeDef",
    "GetMergeCommitOutputTypeDef",
    "GetMergeConflictsOutputTypeDef",
    "GetMergeOptionsOutputTypeDef",
    "GetPullRequestApprovalStatesOutputTypeDef",
    "GetPullRequestOutputTypeDef",
    "GetPullRequestOverrideStateOutputTypeDef",
    "GetRepositoryOutputTypeDef",
    "GetRepositoryTriggersOutputTypeDef",
    "ListApprovalRuleTemplatesOutputTypeDef",
    "ListAssociatedApprovalRuleTemplatesForRepositoryOutputTypeDef",
    "ListBranchesOutputTypeDef",
    "ListPullRequestsOutputTypeDef",
    "ListRepositoriesForApprovalRuleTemplateOutputTypeDef",
    "ListRepositoriesOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "MergeBranchesByFastForwardOutputTypeDef",
    "MergeBranchesBySquashOutputTypeDef",
    "MergeBranchesByThreeWayOutputTypeDef",
    "MergePullRequestByFastForwardOutputTypeDef",
    "MergePullRequestBySquashOutputTypeDef",
    "MergePullRequestByThreeWayOutputTypeDef",
    "PaginatorConfigTypeDef",
    "PostCommentForComparedCommitOutputTypeDef",
    "PostCommentForPullRequestOutputTypeDef",
    "PostCommentReplyOutputTypeDef",
    "PutFileEntryTypeDef",
    "PutFileOutputTypeDef",
    "PutRepositoryTriggersOutputTypeDef",
    "TargetTypeDef",
    "TestRepositoryTriggersOutputTypeDef",
    "UpdateApprovalRuleTemplateContentOutputTypeDef",
    "UpdateApprovalRuleTemplateDescriptionOutputTypeDef",
    "UpdateApprovalRuleTemplateNameOutputTypeDef",
    "UpdateCommentOutputTypeDef",
    "UpdatePullRequestApprovalRuleContentOutputTypeDef",
    "UpdatePullRequestDescriptionOutputTypeDef",
    "UpdatePullRequestStatusOutputTypeDef",
    "UpdatePullRequestTitleOutputTypeDef",
)