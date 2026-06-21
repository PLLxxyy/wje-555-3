export const formatMoney = (value: string | number) => `¥${Number(value || 0).toLocaleString('zh-CN', { minimumFractionDigits: 2 })}`
export const formatDate = (value?: string | null) => (value ? new Date(value).toLocaleDateString('zh-CN') : '-')

