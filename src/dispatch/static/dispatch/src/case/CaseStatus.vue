<template>
  <div>
    <div v-if="status == 'New'">
      <v-badge bordered color="red" slot="activator" dot left offset-x="-10" offset-y="12">
        {{ status }}
      </v-badge>
    </div>
    <div v-if="status == 'Triage'">
      <v-badge bordered color="orange" slot="activator" dot left offset-x="-10" offset-y="12">
        {{ status }}
      </v-badge>
    </div>
    <div v-if="status == 'Escalated'">
      <v-badge bordered color="yellow" slot="activator" dot left offset-x="-10" offset-y="12">
        {{ status }}
      </v-badge>
    </div>
    <div v-if="status == 'Closed'">
      <v-badge bordered color="success" dot left offset-x="-10" offset-y="12">
        {{ status }}
      </v-badge>
    </div>
  </div>
</template>

<script>
export default {
  name: "CaseStatus",

  props: {
    status: {
      type: String,
      required: true,
    },
    id: {
      type: Number,
      required: true,
    },
  },
}
</script>
