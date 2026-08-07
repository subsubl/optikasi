<template>
  <div>
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
  </div>
</template>

<script setup lang="ts">
import { useSeoSchema } from './composables/useSeoSchema';

// Initialize SEO schema
useSeoSchema();
</script>