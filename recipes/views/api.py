from django.shortcuts import get_object_or_404
from recipes.models import Recipe
from recipes.serializers import RecipeSerializer, TagSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from tag.models import Tag


@api_view()
def recipes_api_list(request):
    recipes = Recipe.objects.get_published()[:10]
    serializer = RecipeSerializer(
        instance=recipes,
        many=True,
        context={"context": request}
    )
    return Response(serializer.data)


@api_view()
def recipes_api_detail(request, pk):
    recipe = get_object_or_404(
        Recipe,
        pk=pk
    )
    serializer = RecipeSerializer(
        instance=recipe,
        many=False,
        context={"context": request}
    )

    return Response(serializer.data)


@api_view()
def tag_api_detail(request, pk):
    tag = get_object_or_404(
        Tag,
        pk=pk
    )
    serializer = TagSerializer(instance=tag, many=False)
    return Response(serializer.data)
