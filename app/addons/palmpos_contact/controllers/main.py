# -*- coding: utf-8 -*-
import json
import logging
import traceback

from odoo import http
from odoo.http import Response, request

_logger = logging.getLogger(__name__)


class PalmPOSContactController(http.Controller):

    def _get_cors_headers(self):
        """Return CORS headers for cross-origin requests"""
        return {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type, Accept',
            'Access-Control-Max-Age': '86400',
        }

    @http.route('/api/contact/submit', type='http', auth='public', methods=['POST', 'OPTIONS'], csrf=False)
    def submit_contact_form(self, **kwargs):
        """Handle contact form submissions from the website"""
        # Handle OPTIONS preflight request
        if request.httprequest.method == 'OPTIONS':
            return Response(status=200, headers=self._get_cors_headers())
        
        try:
            # Parse JSON request body
            request_body = request.httprequest.get_data(as_text=True)
            if not request_body:
                raise ValueError('Empty request body')
            
            data = json.loads(request_body)
            params = data.get('params', {})
            
            # Extract form data
            name = params.get('name', '')
            email = params.get('email', '')
            phone = params.get('phone', '')
            subject = params.get('subject', 'Contact Form Submission')
            message = params.get('message', '')
            
            # Validate required fields
            if not name or not email or not message:
                response_data = {
                    'jsonrpc': '2.0',
                    'id': data.get('id'),
                    'result': {
                        'success': False,
                        'message': 'Please fill in all required fields.'
                    }
                }
                return Response(
                    json.dumps(response_data),
                    status=200,
                    headers={**self._get_cors_headers(), 'Content-Type': 'application/json'}
                )
            
            # Prepare email content
            email_body = f"""
                <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
                    <h2 style="color: #10b981;">New Contact Form Submission</h2>
                    <div style="background-color: #f9fafb; padding: 20px; border-radius: 8px;">
                        <p><strong>Name:</strong> {name}</p>
                        <p><strong>Email:</strong> {email}</p>
                        <p><strong>Phone:</strong> {phone}</p>
                        <p><strong>Subject:</strong> {subject}</p>
                        <hr style="border: 1px solid #e5e7eb; margin: 20px 0;">
                        <p><strong>Message:</strong></p>
                        <p style="white-space: pre-wrap;">{message}</p>
                    </div>
                    <p style="color: #6b7280; font-size: 12px; margin-top: 20px;">
                        This email was sent from the PalmPOS website contact form.
                    </p>
                </div>
            """
            
            # Send email using Odoo's email system
            mail_values = {
                'subject': f'[Contact Form] {subject}',
                'body_html': email_body,
                'email_to': 'support@palmposmu.com',
                'email_from': request.env['ir.config_parameter'].sudo().get_param('mail.default.from', 'support@maulist.com'),
                'reply_to': email,
            }
            
            mail = request.env['mail.mail'].sudo().create(mail_values)
            mail.send()
            
            _logger.info(f'Contact form submission from {name} ({email})')
                
                response_data = {
                    'jsonrpc': '2.0',
                    'id': data.get('id'),
                    'result': {
                        'success': True,
                        'message': 'Thank you for your message! We\'ll get back to you shortly.'
                    }
                }
                return Response(
                    json.dumps(response_data),
                    status=200,
                    headers={**self._get_cors_headers(), 'Content-Type': 'application/json'}
                )
            
        except Exception as e:
            _logger.error(f'Error processing contact form: {str(e)}')
            _logger.error(traceback.format_exc())
            response_data = {
                'jsonrpc': '2.0',
                'id': data.get('id', 1) if 'data' in locals() else 1,
                'result': {
                    'success': False,
                    'message': 'An error occurred. Please try again or contact us directly at support@palmposmu.com'
                }
            }
            return Response(
                json.dumps(response_data),
                status=200,
                headers={**self._get_cors_headers(), 'Content-Type': 'application/json'}
            )

    @http.route('/api/contact/pricing-inquiry', type='http', auth='public', methods=['POST', 'OPTIONS'], csrf=False)
    def submit_pricing_inquiry(self, **kwargs):
        """Handle pricing inquiry form submissions"""
        # Handle OPTIONS preflight request
        if request.httprequest.method == 'OPTIONS':
            return Response(status=200, headers=self._get_cors_headers())
        
        try:
            # Parse JSON request body
            request_body = request.httprequest.get_data(as_text=True)
            if not request_body:
                raise ValueError('Empty request body')
            
            data = json.loads(request_body)
            params = data.get('params', {})
            
            # Extract form data
            name = params.get('name', '')
            email = params.get('email', '')
            phone = params.get('phone', '')
            company = params.get('company', '')
            message = params.get('message', '')
            plan_name = params.get('plan_name', '')
            plan_price = params.get('plan_price', '')
            setup_fee = params.get('setup_fee', '')
            
            # Validate required fields
            if not name or not email or not phone or not company:
                response_data = {
                    'jsonrpc': '2.0',
                    'id': data.get('id'),
                    'result': {
                        'success': False,
                        'message': 'Please fill in all required fields.'
                    }
                }
                return Response(
                    json.dumps(response_data),
                    status=200,
                    headers={**self._get_cors_headers(), 'Content-Type': 'application/json'}
                )
            
            # Prepare email content
            email_body = f"""
                <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
                    <h2 style="color: #10b981;">New Pricing Inquiry - {plan_name}</h2>
                    <div style="background-color: #f9fafb; padding: 20px; border-radius: 8px;">
                        <h3 style="color: #059669; margin-top: 0;">Contact Information</h3>
                        <p><strong>Name:</strong> {name}</p>
                        <p><strong>Email:</strong> {email}</p>
                        <p><strong>Phone:</strong> {phone}</p>
                        <p><strong>Company:</strong> {company}</p>
                        
                        <hr style="border: 1px solid #e5e7eb; margin: 20px 0;">
                        
                        <h3 style="color: #059669;">Selected Plan</h3>
                        <p><strong>Plan:</strong> {plan_name}</p>
                        <p><strong>Price:</strong> {plan_price}</p>
                        <p><strong>Setup Fee:</strong> {setup_fee if setup_fee else 'Custom'}</p>
                        
                        {f'''
                        <hr style="border: 1px solid #e5e7eb; margin: 20px 0;">
                        <h3 style="color: #059669;">Additional Message</h3>
                        <p style="white-space: pre-wrap;">{message}</p>
                        ''' if message else ''}
                    </div>
                    <p style="color: #6b7280; font-size: 12px; margin-top: 20px;">
                        This email was sent from the PalmPOS pricing page.
                    </p>
                </div>
            """
            
            # Send email
            mail_values = {
                'subject': f'[Pricing Inquiry] {plan_name} - {company}',
                'body_html': email_body,
                'email_to': 'support@palmposmu.com',
                'email_from': request.env['ir.config_parameter'].sudo().get_param('mail.default.from', 'support@maulist.com'),
                'reply_to': email,
            }
            
            mail = request.env['mail.mail'].sudo().create(mail_values)
            mail.send()
            
            _logger.info(f'Pricing inquiry for {plan_name} from {name} ({company})')
            
            response_data = {
                'jsonrpc': '2.0',
                'id': data.get('id'),
                'result': {
                    'success': True,
                    'message': 'Thank you! We\'ve received your request and will contact you within 24 hours.'
                }
            }
            return Response(
                json.dumps(response_data),
                status=200,
                headers={**self._get_cors_headers(), 'Content-Type': 'application/json'}
            )
            
        except Exception as e:
            _logger.error(f'Error processing pricing inquiry: {str(e)}')
            _logger.error(traceback.format_exc())
            response_data = {
                'jsonrpc': '2.0',
                'id': data.get('id', 1) if 'data' in locals() else 1,
                'result': {
                    'success': False,
                    'message': 'An error occurred. Please try again or contact us directly at support@palmposmu.com'
                }
            }
            return Response(
                json.dumps(response_data),
                status=200,
                headers={**self._get_cors_headers(), 'Content-Type': 'application/json'}
            )
