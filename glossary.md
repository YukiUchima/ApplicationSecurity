### OpenCRE:

    Developed to address complexities and fragmentation with security standards. Provides common language and framework for mapping and comparing various security standards, guidelines, and frameworks

    Purpose: provides uniform landscape as a resource for security

    Functionality: links to common requirements, easier to find relevant info

    Maintenance: self-maintined by auto scanning links to OpenCRE

    Collaboration: software sec profeessionals, OWASP 10, SKF

    Resources: testing guides, OWAS standards, NIST-800 53, ISO27002, etc.

## OWASP TOP 10

### 1 Broken Access Control:

    attackers exploit improperly inforced restrictions to gain access

### 2 Cryptographic Failures:

    poor encryption leading to exposure of data (at rest or in transit)

### 3 Injection:

    flaws (SQL, LDAP) where attacker can query data or send commands without proper authorization

### 4 Insecure Design:

    failed to build secure application in design process through threat modeling, secure design patters or principles

### 5 Security misconfiguration

    commonly due to insecure default configuration, open clouse storage, misconfigured HTTP headers, verbose error messages containing sensitive information

### 6 Vulnerable/Outdated Components

    Components (libraries, frameworks, software modules) that are vulnerable and if exploited, serious data can be loss or server taken over

### 7 Identification and Authentication Failures

    when attackers compromise passwords, keys, session tokens, or assume identities temp or perm

### 8 Software and Data Integrity Failures

    code or infrastructure that doesn't properly protect against integrity failures such as plugins or untrusted sources that lead to a compromise to a system/application/server/etc.

### 9 Insufficient logging/monitoring

    in addition to missing or ineffective integration with incident response, attackers can effectively harm the system, steal data, tamper

### 10 Server-side request forgery (SSRF)

    SSRF occurs when application fetches resources without validating URL, then attacked takes advantage by entering destination of their choosing
