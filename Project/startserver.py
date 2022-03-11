import connexion
from connexion.resolver import RestyResolver

app = connexion.App(__name__, specification_dir = './', options={"swagger_ui": True})
app.add_api('openapi.yaml', resolver = RestyResolver('app.api'))
app.run(port=8080)