SELECT
     cl.id
    ,cl.[version]
    ,cl.dt
    ,cl.issue
    ,cl.issueUrl
    ,cl.[description]
    ,cl.comment
    ,cl.developer
    ,cl.svnCopyTo
    ,cl.svnCommit
    ,cl.isDev
    ,cl.fio
    ,cl.crossIssue
FROM dbo.vChangeLog AS cl
ORDER BY version DESC, dt DESC;
