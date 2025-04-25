## 🐳 Dockerisation

### Prérequis
- Docker Engine 20+
- Docker Compose 2.2+

### 🚀 Exécution

**Mode simple (sans Grid)**
```bash
docker build -t arvea-tests .
docker run --rm -v $(pwd)/reports:/app/reports arvea-tests
```

**Avec Selenium Grid**
```bash
# Démarrer l'infrastructure
docker-compose -f docker/compose.yml up -d --scale chrome=3

# Lancer les tests
docker-compose -f docker/compose.yml run --rm tests pytest -n 3

# Arrêter
docker-compose -f docker/compose.yml down
```

### 🔧 Configuration
Variables d'environnement disponibles :
```env
BROWSER=chrome|firefox
HEADLESS=true|false
TEST_ENV=dev|staging
```
