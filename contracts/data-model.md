# Modelo de Datos del Dominio y Especificaciones de Entidades

Este documento vivo representa la única fuente de verdad (single source of truth) para las entidades de dominio, modelos relacionales y contratos de datos en toda la aplicación.

---

## 1. Diagrama Entidad-Relación (ERD)

```mermaid
erDiagram
    %% Living Diagram - Update as domain entities are introduced
    ORGANIZATION ||--o{ USER : contains
    USER ||--o{ ACCOUNT : owns
    ACCOUNT ||--o{ TRANSACTION : registers

    ORGANIZATION {
        string id PK "UUIDv4"
        string name "Organization Name"
        datetime created_at "Timestamp"
        datetime updated_at "Timestamp"
    }

    USER {
        string id PK "UUIDv4"
        string organization_id FK "References ORGANIZATION(id)"
        string email UK "Unique User Email"
        string full_name "User Full Name"
        string status "ACTIVE | SUSPENDED"
        datetime created_at "Timestamp"
    }

    ACCOUNT {
        string id PK "UUIDv4"
        string user_id FK "References USER(id)"
        string account_number UK "Unique Account Identifier"
        string currency "ISO 4217 Currency Code (e.g. USD, EUR)"
        decimal balance "Current Balance"
        string status "OPEN | FROZEN | CLOSED"
    }

    TRANSACTION {
        string id PK "UUIDv4"
        string account_id FK "References ACCOUNT(id)"
        decimal amount "Transaction Amount (+ / -)"
        string transaction_type "DEBIT | CREDIT | TRANSFER"
        string status "PENDING | COMPLETED | REJECTED"
        datetime executed_at "Timestamp"
    }
```

---

## 2. Esquemas de Entidades e Invariantes

### 2.1 Invariantes de Entidad
1. **Precisión y Monedas**: Todos los montos monetarios deben usar decimales de punto fijo exactos (`decimal` / unidades menores enteras) en lugar de números de punto flotante para evitar artefactos de redondeo.
2. **Inmutabilidad de Transacciones**: Una vez que la entidad `TRANSACTION` alcanza el estado `COMPLETED` o `REJECTED`, sus atributos no pueden ser modificados. Las reversiones compensatorias deben registrarse como eventos de transacción distintos.
3. **Pistas de Auditoría (Audit Trails)**: Todo aggregate root debe mantener marcas de tiempo (timestamps) para `created_at` y `updated_at`.

---

## 3. Protocolos de Migración y Evolución
- Las alteraciones del esquema deben acompañarse de un script de migración ejecutable y la correspondiente actualización en este documento.
- Los cambios de esquema que rompan compatibilidad (breaking changes) requieren planes de transición versionados.
