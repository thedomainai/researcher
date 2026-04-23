# Sidebar Information Architecture

## Question

What should the sidebar express in this product, and what should it explicitly not try to do?

## Problem

The previous sidebar mixed three different jobs:

- product branding
- page explanation
- view navigation

That made the rail feel like a landing page hero squeezed into a navigation column. The result was visually heavy, semantically confused, and duplicated the page identity that already exists in the main content area.

## Decision

The sidebar is a wayfinding surface, not a branding surface.

It should answer only these questions:

1. Which views exist?
2. Which view am I in right now?
3. What shared corpus am I navigating?

It should not contain:

- product title blocks
- marketing copy
- explanatory prose that belongs in the main canvas

## Structure

The new rail is intentionally narrow in meaning:

- `Views`
  The primary switcher between Atlas, Reader, and Index.
- `Corpus snapshot`
  Shared dataset context, not product identity.

## Why This Is Better

- The main area owns page identity and narrative.
- The sidebar owns navigation and shared corpus context.
- Repeated “product title” copy is removed, so the rail reads like an application control surface instead of a promo panel.
- Graph and Reader now share the same navigation semantics.
