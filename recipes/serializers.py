from rest_framework import serializers

from recipes.models import Recipe, Tag


class TagSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=256)
    slug = serializers.SlugField()

    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug']


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'description',
                  'category', 'author',
                  'tags']

        public = serializers.BooleanField(source="is_published")
        preparation = serializers.SerializerMethodField()
        category = serializers.StringRelatedField()
        tag_objects = TagSerializer(many=True, source='tags')
        tag_links = serializers.HyperlinkedRelatedField(
            many=True,
            source="tags",
            queryset=Tag.objects.all(),
            view_name="recipes:recipes_api_v2_tag"
        )

    def get_preparation(self, recipe):
        return f"{recipe.preparation_time} {recipe.preparation_time_unit}"

    def validate(self, attrs):
        context_dictionary = attrs
        return context_dictionary

    def validate_title(self, value):
        ...
