Feature: Búsqueda de películas en IMDb

  Scenario: Buscar la película "Pulp fiction" y validar su calificación
    Given El usuario se encuentra en la página principal de IMDb
    When El usuario busca la película "Pulp fiction"
    And El usuario abre el primer resultado de la búsqueda
    Then La calificación de la película se muestra correctamente
