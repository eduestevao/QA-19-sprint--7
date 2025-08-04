import data
import helpers

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("conectado ao servidor Urban Routes")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução.")

    def test_set_route(self):
        # adicionar em s8
        print("função criada para definir a rota")
        pass

    def test_select_plan(self):
        # adicionar em s8
        print("função criada para definir a seleção de plano")
        pass

    def test_fill_phone_number(self):
        # adicionar em s8
        print("função criada para definir a telefone e numero")
        pass

    def test_fill_card(self):
        # adicionar em s8
        print("função criada para definir  cartão")
        pass

    def test_comment_for_driver(self):
        # adicionar em s8
        print("função criada para definir  comentarios de motorista")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # adicionar em s8
        print("função criada para definir encomendar cobertores e lenços")
        pass

    def test_order_2_ice_creams(self):
        number_of_ice_creams = 2
        for count in range(number_of_ice_creams):
            # adicionar em s8
            print("função criada para definir pedidos de sorvetes")
        pass

    def test_car_search_model_appears(self):
        # adicionar em s8
        print("função criada para definir peesquisa do modelo do carro")
        pass








