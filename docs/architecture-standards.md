> [!NOTE]
> Este estándar arquitectónico es una referencia recomendada. La estructura concreta de directorios dentro de `src/` se define formalmente al configurar [STACK.md](file:///c:/Finance/STACK.md). Si el stack elegido no requiere Clean/Hexagonal Architecture, este documento puede adaptarse.

# Estándares de Arquitectura: Diseño Limpio / Hexagonal por Capas

Este documento establece la base arquitectónica del código. Todas las implementaciones de características (features) deben respetar el aislamiento de límites y las reglas de dependencias definidas aquí.

---

## 1. Filosofía Arquitectónica: Clean / Hexagonal Architecture

El sistema desacopla la lógica central de negocio de los frameworks externos, bases de datos y transportes de red.

```text
                  +---------------------------------------------------+
                  |             INFRASTRUCTURE / ADAPTERS             |
                  |  (HTTP Controllers, CLI, DB Repositories, SDKs)   |
                  +-------------------------+-------------------------+
                                            | depends on
                                            v
                  +---------------------------------------------------+
                  |               USE CASES / APPLICATION             |
                  |     (Orchestration, Transaction Scripts, DTOs)    |
                  +-------------------------+-------------------------+
                                            | depends on
                                            v
                  +---------------------------------------------------+
                  |                 DOMAIN / CORE                     |
                  |        (Entities, Value Objects, Invariants)      |
                  +---------------------------------------------------+
```

### La Regla de Dependencia (Dependency Rule):
**Las dependencias deben apuntar estrictamente hacia adentro.**
- El **Domain** no sabe nada sobre bases de datos, frameworks web o APIs externas.
- La capa de **Application / Use Cases** define interfaces (ports) para persistencia y servicios externos, pero nunca importa implementaciones concretas de la infraestructura.
- La capa de **Infrastructure / Adapters** implementa las interfaces definidas por los Use Cases (Dependency Inversion Principle).

---

## 2. Responsabilidades por Capa

### 2.1 Capa de Dominio (Domain Layer) (`src/domain/`)
- Contiene lógica pura de negocio: Aggregate Roots, Entities, Value Objects y Domain Events.
- **Restricciones**: Cero dependencias de runtime de terceros (sin decoradores ORM, sin objetos de request de frameworks).
- Todas las invariantes de negocio y transiciones de estado se validan aquí.

### 2.2 Capa de Aplicación / Casos de Uso (Application / Use Cases Layer) (`src/application/`)
- Orquesta flujos de trabajo de negocio y coordina entidades del Domain.
- Define objetos Command / Query e Interface Ports (ej. `UserRepositoryPort`, `NotificationServicePort`).
- Maneja los límites transaccionales y la verificación de permisos.

### 2.3 Capa de Adaptadores e Infraestructura (Adapters & Infrastructure Layer) (`src/infrastructure/` / `src/adapters/`)
- Proporciona implementaciones concretas para los Ports definidos en la capa de Aplicación.
- Contiene controladores HTTP, objetos de acceso a bases de datos, consumidores de colas de mensajes y clientes de APIs externas.
- Responsable de transformar los payloads de transporte externo (JSON/Protobuf) a DTOs internos.

---

## 3. Reglas de Scope Creep y Anti-Vibecoding
1. **Sin abstracciones especulativas**: No crear arquitecturas generalizadas de plugins o capas de abstracción multi-inquilino (multi-tenant) a menos que esté explícitamente dictado en `.specs/approved/`.
2. **Contract-first enforcement**: Cualquier endpoint expuesto en adaptadores debe coincidir con el schema en [contracts/api-spec.yml](file:///c:/Finance/contracts/api-spec.yml).
