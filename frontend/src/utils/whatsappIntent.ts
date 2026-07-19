import type { CartItem } from '@/types/order'
import { formatCurrency } from '@/utils/formatCurrency'

/**
 * Builds a wa.me deep link with the order pre-filled in the message text,
 * so the customer doesn't have to retype their cart when they land in chat.
 */
export function buildWhatsAppOrderUrl(
  whatsappNumber: string,
  orderId: string,
  items: CartItem[],
  totalAmount: string,
): string {
  const lines = [
    `Hi RajwadiTukda! I'd like to complete order ${orderId.slice(0, 8)}:`,
    ...items.map((item) => `- ${item.product_name} x ${item.quantity}`),
    `Total: ${formatCurrency(totalAmount)}`,
    '',
    "Here's my name, phone number, and delivery address (Jaipur only):",
  ]
  const text = encodeURIComponent(lines.join('\n'))
  return `https://wa.me/${whatsappNumber}?text=${text}`
}
