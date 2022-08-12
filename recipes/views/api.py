from django.shortcuts import get_object_or_404
from recipes.models import Recipe
from recipes.serializers import RecipeSerializer, TagSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from tag.models import Tag


@api_view(http_method_names=['GET', 'POST'])
def recipes_api_list(request):
    if request.method == 'GET':
        recipes = Recipe.objects.get_published()[:10]
        serializer = RecipeSerializer(
            instance=recipes,
            many=True,
            context={"context": request}
        )
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RecipeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()


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
