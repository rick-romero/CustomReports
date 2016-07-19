from openerp import api, models
import logging
class ParticularReport(models.AbstractModel):
    _name = 'report.reports_crm.report_all_leads'
    _template = 'reports_crm.report_all_leads'
    _logger = logging.getLogger(__name__)
    
    @api.multi
    def render_html(self, data=None):
        
        report_obj = self.env['report']
        report = report_obj._get_report_from_name(self._template)
        
        self._logger.debug(self._ids)
        self._logger.debug(report.model)
        
        docargs = {
            'doc_ids': self._ids,
            'doc_model': report.model,
            'docs': self,
        }
        return report_obj.render(self._template, docargs)
ParticularReport()