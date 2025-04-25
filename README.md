## 🚀 Exécution des Tests

### Localement
```bash
pytest tests/ -v --html=report.html
```

### Via Docker (Selenium Grid)
```bash
# Lancer les containers
docker-compose -f docker/compose.yml up -d

# Exécuter les tests
docker-compose -f docker/compose.yml run tests

# Arrêter tout
docker-compose -f docker/compose.yml down
```
