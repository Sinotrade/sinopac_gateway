from vnpy.event import EventEngine
from vnpy.trader.engine import MainEngine
from vnpy.trader.ui import MainWindow, create_qapp
from vnpy.app.cta_strategy import CtaStrategyApp
from vnpy.app.cta_backtester import CtaBacktesterApp
from vnpy.app.algo_trading import AlgoTradingApp
from vnpy.app.data_recorder import DataRecorderApp
from vnpy.app.spread_trading import SpreadTradingApp
from vnpy.app.script_trader import ScriptTraderApp
from vnpy.app.risk_manager import RiskManagerApp
from vnpy.gateway.sinopac import SinopacGateway


def main():
    """Start VN Trader"""
    qapp = create_qapp()

    event_engine = EventEngine()
    main_engine = MainEngine(event_engine)

    main_engine.add_gateway(SinopacGateway)
    main_engine.add_app(CtaStrategyApp)
    main_engine.add_app(CtaBacktesterApp)
    main_engine.add_app(AlgoTradingApp)
    main_engine.add_app(DataRecorderApp)
    main_engine.add_app(SpreadTradingApp)
    main_engine.add_app(ScriptTraderApp)
    main_engine.add_app(RiskManagerApp)

    main_window = MainWindow(main_engine, event_engine)
    main_window.showMaximized()

    qapp.exec()


if __name__ == "__main__":
    main()
