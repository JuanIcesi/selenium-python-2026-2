Feature: Lobby login

  Scenario: Validar ingreso exitoso al lobby
    Given El usuario se encuentra en la página de login
    When El usuario ingresa con un nombre único
    Then El nombre único del usuario aparece en el dashboard

  Scenario: Validar mensaje de error al intentar ingresar con un nombre de usuario que contiene espacios
    Given El usuario se encuentra en la página de login
    When El usuario ingresa con el nombre "Juan Pablo"
    Then El mensaje de error "Usa entre 3 y 20 caracteres: letras sin tildes, números, guion o guion bajo." aparece en el login
