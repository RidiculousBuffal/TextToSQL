export function areAllPropertiesDefined(obj:Object) {
    return Object.values(obj).every(value => value !== null && value !== undefined);
}