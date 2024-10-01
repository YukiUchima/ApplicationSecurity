# ----------------------- SDLC --------------------
# Requirements - Customer
# Design - Senior Engineer or Architect
# Development and Implementation - Work actually done
# Test - unit tests (dev environment)
    # regression issues
    # systems test
    # integration tests
# Ops - various environements 
    # Dev - testing environment
    # UAT - quality assurance
    # Prod - client can access to finished product
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


# ----------------------------------------------
# Security must be integrated somewhere in SDLC

# -> Requirements    
    # Reference Arch
    # Standards
    # Frameworks
# Security
    # Security Requirements
# DESIGN
        # Security in design
        # Security Model - goal is to check what can go wrong and remediate
# AST (Application Sec Tools/Testing)
    # Implement tools by dev to create secure software
    # Static analysis
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# ------------------------ OWASP TOP 10
# Web Application Top 10 (most known)
# Other TOP 10:
    # API Security
    # Data Security
    # Low-Code/No-Code
    # Mobile
    # Serverless Architectures
    # CI/CD - Continuous integration continuous deployment env
    # LLM
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# -------------------- Security Goals
# Must consider the nature of IT assets and capabilities when considering security goals

# -------------------- CIA
# Confidentiality: information accessed by authorized users
# Integrity: maintain data from corruption
# Availabilility: Accessible when needed

# Security Principles
    # -> Economy of Mechanism
        # keep it simple
    # -> Fail-safe defaults
        # fall back to most secure option
    # -> Complete Mediation
        # check every access to a resource for authority
    # -> Open design
        # there's no security through obscurity
    # -> Separation of privilege
        # two keys are more secure than one
    # -> Least Privilege
        # ensure access to only what is required
    # -> Lease Common Mechanism
        # reduce shared components in a system
    # -> Psychological acceptability
        # make it easy to practice security for people