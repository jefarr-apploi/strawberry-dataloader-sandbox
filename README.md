# Strawberry Dataloaders

[docs](https://strawberry.rocks/docs/guides/dataloaders)
[source code](https://github.com/strawberry-graphql/strawberry/blob/0.205.0/strawberry/dataloader.py)

This is a simple sandbox for experimenting with Dataloaders, it replicates a common pattern used at Apploi, but in this case via a "Users and Roles" schema as an example.

To run the app and see the logs:

``` shell
docker compose build
docker compose up flaskapp
```

Then in another tab:

``` shell
docker compose run gqltest
cat api.log
```

Things to look out for when designing a dataloader:

- A dataloader _must_ return the same number of values (in the same order!) as keys that are passed into it.  Otherwise a (WrontNumberOfResultsReturned)[https://github.com/strawberry-graphql/strawberry/blob/0.205.0/strawberry/dataloader.py#L255] exception will be thrown.
