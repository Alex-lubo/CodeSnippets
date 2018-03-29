Use a filter
Place filters in the right place. (Probably in a filtered-query!)


Combine filters with bool.and not and or or
Order filters by their selectivity.

filter:
  And/Or/Not work on a doc-by-doc basis. They first load whatever data is needed into the Field Data memory pool then iterate over the docs, excluding as they go.


In particular, joins should be avoided. nested can make queries several times slower and parent-child relations can make queries hundreds of times slower. So if the same questions can be answered without joins by denormalizing documents, significant speedups can be expected.


The following points summarize tips for maximizing the performance of Elasticsearch queries:
'Avoid queries that involve wild cards wherever possible.
```If the same field is subject to full-text searching and exact matching, then consider storing the data for the field in analyzed and nonanalyzed forms. Perform full-text searches against the analyzed field, and exact matches against the nonanalyzed field.
```Only return the data necessary. If you have large documents, but an application only requires information held in a subset of the fields, then return this subset from queries rather than entire documents. This strategy can reduce the network bandwidth requirements of the cluster.
```Wherever possible, use filters instead of queries when searching for data. A filter simply determines whether a document matches a given criterion whereas a query also calculates how close a match a document is (scoring). Internally, the values generated by a filter are stored as a bitmap indicating match/no match for each document, and they can be cached by Elasticsearch. If the same filter criterion occurs subsequently, the bitmap can be retrieved from cache and used to quickly fetch the matching documents. For more information, see Internal Filter Operation.
Use bool filters for performing static comparisons, and only use and, or, and not filters for dynamically calculated filters, such as those that involve scripting or the geo-\* filters.
If a query combines bool filters with and, or, or not with geo-* filters, place the and/or/not geo-* filters last so that they operate on the smallest data set possible.
Similarly, use a post_filter to run expensive filter operations. These filters will be performed last.
Use aggregations rather than facets. Avoid calculating aggregates that are analyzed or that have many possible values.
Note: Facets have been removed in Elasticsearch version 2.0.0.
Use the cardinality aggregation in preference to the value_count aggregation unless your application requires an exact count of matching items. An exact count can become quickly outdated, and many applications only require a reasonable approximation.
Avoid scripting. Scripts in queries and filters can be expensive and the results are not cached. Long-running scripts can consume search threads indefinitely, causing subsequent requests to be queued. If the queue fills up, further requests will be rejected.