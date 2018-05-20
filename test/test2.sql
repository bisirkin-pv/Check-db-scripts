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
FROM OPENQUERY (DBWSH, 'SELECT * FROM dbo.vChangeLog') AS cl
ORDER BY version DESC, dt DESC;

SELECT
    cl.id
FROM SERVER.BASE.dbo.text
