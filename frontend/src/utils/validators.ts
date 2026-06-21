export const requiredRule = (message = '请填写必填项') => [{ required: true, message, trigger: 'blur' }]
export const selectRule = (message = '请选择') => [{ required: true, message, trigger: 'change' }]

