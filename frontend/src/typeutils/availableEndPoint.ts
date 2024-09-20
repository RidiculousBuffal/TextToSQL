const availableEndpoints = ['/chatWithSQL'] as const
export type AllowedEndpoint = typeof availableEndpoints[number]