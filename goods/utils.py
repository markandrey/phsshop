import keyword
from django.db.models import Q
from django.contrib.postgres.search import (
    SearchQuery,
    SearchRank,
    SearchVector,
    TrigramSimilarity,
    SearchHeadline,
)
from goods.models import Product


def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Product.objects.filter(id=int(query))

    vector = SearchVector("name", "description", config="russian")
    search_query = SearchQuery(query, config="russian")

    # Добавляем триграммное сходство
    return (
        Product.objects.annotate(
            search=vector,
            rank=SearchRank(vector, search_query),
            similarity=TrigramSimilarity("name", query)
            + TrigramSimilarity("description", query),
            name_headline=SearchHeadline(
                'name',
                search_query,
                start_sel='<mark>',
                stop_sel='</mark>',
                config='russian'
            ),
            description_headline=SearchHeadline(
                'description',
                search_query,
                start_sel='<mark>',
                stop_sel='</mark>',
                config='russian'
            )
        )
        .filter(Q(rank__gte=0.1) | Q(similarity__gt=0.1))
        .order_by("-rank", "-similarity")
    )
