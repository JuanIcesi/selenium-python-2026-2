from behave import given, when, then
from pages.imdb_search_page import ImdbSearchPage
from pages.imdb_movie_page import ImdbMoviePage


@given('El usuario se encuentra en la página principal de IMDb')
def step_given_user_on_imdb_page(context):
    context.imdb_search_page = ImdbSearchPage(context.driver)
    context.imdb_search_page.open()


@when('El usuario busca la película "{movie}"')
def step_when_user_searches_movie(context, movie):
    context.imdb_search_page.search_movie(movie)


@when('El usuario abre el primer resultado de la búsqueda')
def step_when_user_opens_first_result(context):
    context.imdb_search_page.open_first_result()
    context.imdb_movie_page = ImdbMoviePage(context.driver)


@then('La calificación de la película se muestra correctamente')
def step_then_movie_rating_is_displayed(context):
    rating = context.imdb_movie_page.get_rating()
    rating_value = float(rating.splitlines()[0])
    assert "/10" in rating
    assert 0 <= rating_value <= 10
