# DeviceDeltaApplyOutcomeType

Result reported by the agent for an update target. NotRequired means the existing target image satisfies the agent's image pull rules, so no delta or pull was needed. NotUsed means the agent skipped delta application without a delta-apply failure; it may still use a full image pull. Applied means all delta work for the target succeeded. Fallback means a delta attempt failed and the agent attempted a full image pull. Partial means an application applied at least one delta while another image target used a full image pull or skipped delta application.

## Enum

* `DeviceDeltaApplyOutcomeNotUsed` (value: `'NotUsed'`)

* `DeviceDeltaApplyOutcomeNotRequired` (value: `'NotRequired'`)

* `DeviceDeltaApplyOutcomeApplied` (value: `'Applied'`)

* `DeviceDeltaApplyOutcomeFallback` (value: `'Fallback'`)

* `DeviceDeltaApplyOutcomePartial` (value: `'Partial'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
